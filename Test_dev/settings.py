"""
Django settings for Test_dev project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import datetime
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '79qnm(sc@25cx6(gqmy_d!16$f83e^1w!5e1m21-z(#bew)1@t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',


    'register',  # 用户注册
    'reptile',  # 爬虫
    'data_detection',  # 数据检测
    'pets',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'utils.handle_middilewares.DeclineSpidersMiddleware'  # 禁止爬虫
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'Test_dev.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '/dist')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# 前端静态文件配置路径
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "/dist/static")]

WSGI_APPLICATION = 'Test_dev.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'test_dev',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         'USER': 'root',
#         'PASSWORD': '123456',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_dev',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '123456',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True
# 时区，False为本地
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'NON_FIELD_ERRORS_KEY': 'errors',

    # 可以修改默认的渲染类（处理返回的数据形式）
    # 列表中的元素有优先级，第一个元素的优先级最高
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.backends.DjangoFilterBackend',
        # 'rest_framework.filters.OrderingFilter',  # 不太适合在全局使用
    ],  # 指定所有视图公用的过滤引擎，如果视图中指定了过滤引擎就使用视图当中的过滤引擎

    # 可以试用默认的分页引擎类PageNumberPagination
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',  # 分页功能
    # 必须指定每一页的数据数量
    'PAGE_SIZE': 10,

    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',  # 解决打开接口文档地址时候报错get_link

    # 认证与权限
    'DEFAULT_AUTHENTICATION_CLASSES': [  # 默认的认证类
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # 指定使用jwt_token认证方式
        'rest_framework.authentication.SessionAuthentication',  # 会话认证
        'rest_framework.authentication.BasicAuthentication'  # 基本认证（用户名和密码认证）
    ],

    # 登录权限设置，账户级别实在auth_user内的is_staff设置
    'DEFAULT_PERMISSION_CLASSES': [  # 默认的权限类
        'rest_framework.permissions.AllowAny',  # AllowAny不需要登录就有任意权限
        # 'rest_framework.permissions.IsAuthenticated',  # IsAuthenticated只要登录就有任意权限
        # 'rest_framework.permissions.IsAdminUser',  # IsAdminUser只有管理员账号登录就有任意权限
    ],
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# CORS_ORIGIN_WHITELIST = (
#     '8.131.51.224:8000',
# )

# CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken'
)

# 在全局配置JWT_AUTH中，可以覆盖JWT相关的参数
JWT_AUTH = {
    # 指定处理登录接口响应数据的函数
    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'utils.jwt_handle.jwt_response_payload_handler',

    # 前端用户访问一些需要认证之后的接口，那么默认需要在请求头中携带参数，
    # 请求key为Authorization，值为前缀 + 空格 + token值，如：JWT xxxssdhdsohsoshsohs

    # 可以指定token过期时间，默认为5分钟
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),

    # 指定前端传递token值的前缀
    # 'JWT_AUTH_HEADER_PREFIX': 'Bearer',
}