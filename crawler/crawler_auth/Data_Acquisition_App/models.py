
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from django_mongoengine import Document, EmbeddedDocument
from django_mongoengine import fields

import datetime
""" """
SCHEDULING_CHIOCE=      (("0"),("one time only"),
                            ("1"),(""),
                            ("2"),(""),
                            ("3"),(""),
                            ("4"),(""),
                            ("5"),(""),
                            ("6"),(""),)




class Twitter_Target_Document(Document):
    target_platform       =fields.StringField(verbose_name="Target_Platform", max_length=255,default="twitter")
    target_type           =fields.StringField(verbose_name="Target_Type",default="tweets",)
    target_username       =fields.StringField(verbose_name="Target_Username",primary_key=True)
    target_scheduling     =fields.StringField(verbose_name="Target_Scheduling",choices=SCHEDULING_CHIOCE)
    scanning_status       =fields.StringField(verbose_name="Scanning_Status",default="pending")
    # tweets              = fields.ListField(
    #                                         fields.EmbeddedDocumentField('Tweet'),
    #                                         default=[],
    #                                         blank=True,
    #                                          )
    created_at            =fields.DateField(default=datetime.datetime.now, editable=False,)
    updated_at            =fields.DateField(default=datetime.datetime.now, editable=True,)
   
    """ Create / Insert """
    def Create_Twitter_Target(self,target_platform,target_type,target_username,twitter_scheduling,scanning_status):
        self.target_platform=target_platform
        self.target_type=target_type
        self.target_username=target_username
        self.twitter_scheduling=twitter_scheduling
        self.scanning_status=scanning_status
        try:
            if(self.save):
                return True
            else:
                return False
        except Exception as e:
            print("Failed to insert Twitter Target Document")
            print(e)
            return False

    """ returns all twitter targets """
    @staticmethod
    def Get_All_Twitter_Targets():
        try:
            Twitter_Target_Document.objects.all()
        except Exception as e:
            print("Get_All_Twitter_Targets --failed")
            print(e) 


    """ returns all twitter targets """
