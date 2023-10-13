from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete,post_delete,post_save,post_init


@receiver(user_logged_in,sender=User)
def user_log(sender,request,user,**kwargs):
    print("This is workimg")
    print(user.password,"------------------ ")


# user_logged_in.connect(user_log, sender=User)

@receiver(pre_save,sender=User)
def before_save(sender,instance,**kwargs):
    print("pre_save")
    print(instance)

@receiver(post_save,sender=User)
def after_save(sender,instance,created,update_fields,**kwargs):
    print("after_save")
    print(instance)
    print(created)
    print(update_fields)

@receiver(pre_delete,sender=User)
def before_delete(sender,instance,using,origin,**kwargs):
    print("before_delete")
    print(instance)
    print(origin)
    print(using)


@receiver(post_delete,sender=User)
def after_delete(sender,instance,using,origin,**kwargs):
    print("after_delete")
    print(instance)
    print(origin)


# @receiver(pre_init,sender=User)
# def after_delete(sender,instance,using,origin,**kwargs):
#     print("after_delete")
#     print(instance)
#     print(origin)


@receiver(post_init,sender=User)
def after_init(sender,instance,**kwargs):
    print("after_init")
    print(instance)