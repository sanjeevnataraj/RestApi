from django.core.management.base import BaseCommand, CommandError
from api.models import User, ActivityPeriod
from django.utils import timezone
import random
import pytz

class Command(BaseCommand):

    def handle(self, *args, **options):
        tz_list = ['America/Santo_Domingo', 'Asia/Samarkand', 'Australia/Brisbane', 
              'America/Indiana/Indianapolis', 'Etc/GMT+10', 'Etc/GMT-9', 
              'America/La_Paz', 'Asia/Pyongyang', 'NZ', 'America/Caracas', 'Europe/Podgorica', 'America/Martinique', 'WET', 'Pacific/Midway', 'ROK', 'CET', 'Asia/Gaza', 'Africa/Asmara', 'America/Mendoza', 'Europe/Luxembourg', 'Africa/Ndjamena', 'Indian/Reunion',
              'Europe/Berlin', 'Europe/Belgrade', 'Australia/Queensland', 
              'US/Pacific', 'Indian/Mauritius'] 
        
        for i in range(100,200):
            id = 'WX01T00'+str(i)
            real_name = "Testuser00"+str(i)
            tz = random.choice(tz_list)
            py_tz = pytz.timezone(tz)
            start_time = datetime.datetime.now(tz=py_tz)
            end_time = datetime.datetime.now(tz=py_tz)
            user_obj = User.objects.create(id=id,real_name=real_name,tz=tz)
            ActivityPeriod.objects.create(uid=user_obj,start_time=start_time,end_time=end_time)
        self.stdout.write(self.style.SUCCESS('Dummy data added sucessfully successfully'))