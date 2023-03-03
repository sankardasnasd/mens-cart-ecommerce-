from django.contrib.auth.forms import SetPasswordForm
from django.urls import path
from.import views
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MySetPasswordForm, MypasswordChangeForm, MypasswordResetForm


urlpatterns = [
    path('passionapp',views.passionapp),
    path('home',views.home,name="home"),
    path('category/<slug:val>',views.CategoryView.as_view(),name="category"),
    path('productdetail/<int:pk>',views.ProductDetail.as_view(),name="productdetail"),
    path('categorytitle<val>',views.CategoryTitle.as_view(),name="categorytitle"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address',views.address,name='address'),
    path('updateAddress/<int:pk>',views.updateAddress.as_view(),name='updateAddress'),

    # cart part
    path('add-to-cart',views.add_to_cart,name = 'add-to-cart'),
    path('cart',views.show_cart,name='showcart'),
    path('checkout',views.show_cart,name='checkout'),
    


    # login authentication
    path('registration',views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('login', auth_view.LoginView.as_view(template_name = 'login.html',authentication_form = LoginForm),name='login'),
    
    path('passwordchange',auth_view.PasswordChangeView.as_view(template_name = 'changepassword.html',form_class = MypasswordChangeForm,success_url = 'passwordchangedone'),name = 'passwordchange'),
    path('passwordchangedone',auth_view.PasswordChangeDoneView.as_view(template_name = 'passwordchangedone.html'),name='passwordchangedone'),
    path('logout',auth_view.LogoutView.as_view(next_page = 'login'),name='logout'),

    path('password_reset',auth_view.PasswordResetView.as_view(template_name = 'password_reset.html',form_class=MypasswordResetForm),name='password_reset'),

    path('password_reset_done',auth_view.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'),name='password_reset_done'),

    path('password_reset-confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    
    path('password_reset-complete',auth_view.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'),name='password_reset_complete'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)