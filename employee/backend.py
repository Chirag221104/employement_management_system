from datetime import datetime, timedelta
from django.contrib.sessions.backends.base import SessionBase
from .models import CustomSession

class CustomSessionStore(SessionBase):
    def load(self):
        try:
            session = CustomSession.objects.get(session_key=self.session_key, expire_date__gt=datetime.now())
            return self.decode(session.session_data)
        except CustomSession.DoesNotExist:
            return {}

    def exists(self, session_key):
        return CustomSession.objects.filter(session_key=session_key).exists()

    def create(self):
        self.session_key = self._get_new_session_key()
        self.modified = True
        self.save(must_create=True)

    def save(self, must_create=False):
        expire_date = datetime.now() + timedelta(seconds=self.get_expiry_age())
        CustomSession.objects.update_or_create(
            session_key=self.session_key,
            defaults={'session_data': self.encode(self._get_session(no_load=must_create)), 'expire_date': expire_date}
        )

    def delete(self, session_key=None):
        if session_key is None:
            if self.session_key is None:
                return
            session_key = self.session_key
        CustomSession.objects.filter(session_key=session_key).delete()
