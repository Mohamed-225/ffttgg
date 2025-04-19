from django.contrib import admin
from django.urls import path
from AIwave import views

# Aliases لتفادي تعديل أسماء الدوال الأصلية
return_policy = views.RETURN_POLICY
terms_conditions = views.terms_conditions

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index),
    path('roadmap', views.roadmap),
    path('utilize', views.utilize),

    # Pages
    path('pages/style-guide', views.styleGuide),
    path('pages/blog', views.blog),
    path('pages/blog-details', views.blogDetails),
    path('pages/pricing', views.pricing),
    path('pages/contact', views.contact),
    path('pages/signin', views.signin),
    path('pages/signup', views.signup),
    path('pages/RETURN-POLICY', return_policy),
    path('pages/terms-conditions', terms_conditions),
    path('pages/privacy-policy', views.privacyPolicy),
    path('pages/profile-details', views.profileDetails),
    path('pages/notification', views.notification),
    path('pages/chat-export', views.chatExport),
    path('pages/appearance', views.appearance),
    path('pages/plans-billing', views.plansBilling),
    path('pages/sessions', views.sessions),
    path('pages/application', views.application),
    path('pages/release-notes', views.releaseNotes),
    path('pages/help', views.help),

    # Tools
    path('tools/text-generator', views.textGenerator),
    path('tools/image-generator', views.imageGenerator),
    path('tools/code-generator', views.codeGenerator),
    path('tools/image-editor', views.imageEditor),
    path('tools/video-generator', views.videoGenerator),
    path('tools/email-generator', views.emailGenerator),
]
