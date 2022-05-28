# yaha kaam karne ke baad ham apps.py par jayege.

from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.dispatch import receiver
from django.contrib.auth.models import User

from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate

from django.db.backends.signals import connection_created

from django.core.signals import request_started, request_finished, got_request_exception

@receiver(user_logged_in,sender=User)
def login_sucess(sender,request,user,**kwargs):
    print("User logged in successfully")
    print("Logged in ..... Run Intro")
    print("Sender : ",sender)
    print("request : ",request)
    print("user : ",user)
    print("Password : ",user.password)
    print(f"kwargs :{kwargs}")
    # print("kwargs :",kwargs)


@receiver(user_logged_out,sender=User)
def logout_finish(sender,request,user,**kwargs):
    print("User Logout in successfully")
    print("Logout ho gaya ..... finish")
    print("Sender : ",sender)
    print("request : ",request)
    print("user : ",user)
    print(f"kwargs :{kwargs}")


@receiver(user_login_failed)
def login_failed(sender,credentials,request,**kwargs):
    print("User Login failed")
    print("Login failed ho gaya ..... fir se kero")
    print("Sender : ",sender)
    print("credentials : ",credentials)
    print("request : ",request)
    print(f"kwargs :{kwargs}")


# user_logged_in.connect(login_sucess,sender=User)
# ham ye kaam decorator se bhi kar sakte h.


@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
 print("----------------------------")
 print("Pre Save Signal...")
 print("Sender:", sender)
 print("Instance:", instance)
 print(f'Kwargs: {kwargs}')
# pre_save.connect(at_beginning_save, sender=User)

#                   yaha model ka name aayega.
@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
 if created:
  print("----------------------------")
  print("Post Save Signal...")
  print("New Record")
  print("Sender:", sender)
  print("Instance:", instance)
  print("Created:", created)
  print(f'Kwargs: {kwargs}')
 else:
  print("----------------------------")
  print("Post Save Signal...")
  print("Update")
  print("Sender:", sender)
  print("Instance:", instance)
  print("Created:", created)
  print(f'Kwargs: {kwargs}')
# post_save.connect(at_ending_save, sender=User)


@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
 print("-----------------------------------------")
 print("Pre Delete Signal......")
 print('Sender:', sender)
 print('Instance:', instance)
 print(f'Kwargs: {kwargs}')
# pre_delete.connect(at_beginning_delete, sender=User)



@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
 print("-----------------------------------------")
 print("Post Delete Signal......")
 print('Sender:', sender)
 print('Instance:', instance)
 print(f'Kwargs: {kwargs}')
# post_delete.connect(at_ending_delete, sender=User)


@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
 print("-----------------------------------------")
 print("before_install_app......")
 print('Sender:', sender)
 print('App_config:', app_config)
 print('Verbosity:', verbosity)
 print('Interactive:', interactive)
 print('Using:', using)
 print('Plan:', plan)
 print('App:', apps)
 print(f'Kwargs: {kwargs}')
# pre_migrate.connect(before_install_app)

@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
 print("-----------------------------------------")
 print("at_end_migrate_flush......")
 print('Sender:', sender)
 print('App_config:', app_config)
 print('Verbosity:', verbosity)
 print('Interactive:', interactive)
 print('Using:', using)
 print('Plan:', plan)
 print('App:', apps)
 print(f'Kwargs: {kwargs}')
# post_migrate.connect(at_end_migrate_flush)



@receiver(connection_created)
def conn_db(sender, connection, **kwargs):
#  py manage.py runserver    --- > tab ye chalega.
 print("-----------------------------------------")
 print("Initial connection to the database......")
 print('Sender:', sender)
 print('Connection:', connection)
 print(f'Kwargs: {kwargs}')
# connection_created.connect(conn_db)


@receiver(got_request_exception)
def at_req_exception(sender, request, **kwargs):
 print("-----------------------------------------")
 print("At Request Exception......")
 print('Sender:', sender)
 print('Request:', request)
 print(f'Kwargs: {kwargs}')
# got_request_exception.connect(at_req_exception)



@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
 print("-----------------------------------------")
 print("Pre Init Signal......")
 print('Sender:', sender)
 print(f'Args: {args}')
 print(f'Kwargs: {kwargs}')
# pre_init.connect(at_beginning_init, sender=User)

@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
 print("-----------------------------------------")
 print("Post Init Signal......")
 print('Sender:', sender)
 print(f'Args: {args}')
 print(f'Kwargs: {kwargs}')
# post_init.connect(at_ending_init, sender=User)

@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
 print("-----------------------------------------")
 print("At Beginning Request......")
 print('Sender:', sender)
 print('Environ:', environ)
 print(f'Kwargs: {kwargs}')
# request_started.connect(at_beginning_request)

@receiver(request_finished)
def at_ending_request(sender, **kwargs):
 print("-----------------------------------------")
 print("At Ending Request......")
 print('Sender:', sender)
 print(f'Kwargs: {kwargs}')
# request_finished.connect(at_ending_request)