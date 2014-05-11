This is a Django 1.6 site. It will probably never be updated.

There are some dependencies. I ought to make a proper [requirements file](https://pip.pypa.io/en/latest/reference/pip_install.html#requirements-file-format), really. To give you a clue, this is what part of `yorkunion/settings.py` might look like:

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sitemaps',
        'django_markwhat',
        'geoposition',
        'events',
        'south'
    )

`geoposition` allows events to be associated with geographical coordinates (on the front end, the University of York's map tile server has been cheekily used). `django_markwhat` is useful for making HTML out of Textile- or Markdown-formatted text. `south` is not strictly necessary, and Django 2.7 will include the same functionality (database schema migrations, for when models are changed) built-in.

`yorkunion` is the main app but `events` contains most of the functionality: events (with associated locations and speakers) can be defined, as well as press cuttings. The templates attempt to support [microdata](https://support.google.com/webmasters/answer/164506). There were grand plans for an iCalendar feed, and to archive the results of votes on motions.

    ROOT_URLCONF = 'yorkunion.urls'
    
    WSGI_APPLICATION = 'yorkunion.wsgi.application'

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    LANGUAGE_CODE = 'en-gb'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = False
    
    STATIC_URL = '/static/'
    
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'django.contrib.staticfiles.finders.FileSystemFinder',
    )
    
    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.core.context_processors.tz",
        "django.contrib.messages.context_processors.messages",
        "django.core.context_processors.request" # non-default
    )

Perhaps the most valuable parts are the reasonable-quality copies of the York Union central hall logo, which used to be the Nouse logo. Here's the ASCII version, rescued from an old Nouse server:

                                                `/yd                                
                                               omo:N:                               
                                              `N+  yy                               
                                              sm`  :N`                              
                                             .N+    N/                              
                                      :smhs/-sm`    sh                              
                                   .odNMMMMNNNmo/.  -N.                             
                                `/hNMMMMMMMMMMMMNNdy+No                             
              ```...-::://++oosymNMMMMMMMMMM+/+oyhddmNNds/.                         
            -smmmmmNNNNNMMMMMMMMMMMMMMMMMMMM-     ``..-:/o/                         
         `:hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/-...`                                  
       .+dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmmmddhhysso++/::---..```             
     -smMMMMMMMMMMMMMMMNNNNmmmmmddddhhyyyysossyhhddmmmNNMMMMMMMNNNmmmdddhho`        
    hNMMMMMMMMd+///:---------------------::/     ```...---://oosyyhhdddmNMMh-       
    MMMMMMMMMMs  ossyyyhhddddddmmmmmNNNNNNMM`                       ```.-hNMmo++++- 
    MMMMMMMMMMy  NMMMMMMMMMMMMMMMMMMMMMMMMMM`                            `+NMMMMMMNs
    MMMMMMMMMMm: :hNMMMMMMMMMMMMMMMMMMMMMMMM`                     -ssssso  -o++++sNN
    NMMMMMMMMMMNy.`+mMMMMMMMMMMMMMMMMMMMMMMM`                     /MMMMd-         -h
    /hNMMMMMMMMMMm+`.yNMMMMMMMMMMMMMMMMMMMMM                  ::::sMMNs`            
      -odNMMMMMMMMMd-`/mMMMMMMMMMMMMMMMMMMMM                 `NMMMMMm/              
         :smNMMMMMMMNs``sMMMMMMMMMMMMMMMMMMM              ```.NMMMNy.               
           `/hNMMMMMMMy  mMMMMMMMMMMMMMMMMMM             .ddddMMMN+                 
              .+dMMMMMy  mMMMMMMMMMMMMMMMMMM             -MMMMMMd-                  
                 mMMMMy  mMMMMMMMMMMMMMMMMMM             `hNMMMM.                   
                 mMMMMy  mMMMMMMMMMMMMMMMMMM               .yMMM.                   
                 mMMMMy  mMMMMMMMMMMMMMMMMMM                +MMM.                   
             .yyyNMMMMmyyNMMMMMMMMMMMMMMMMMMddddddddddddddddmMMMdh.                 
             -MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM-                 
