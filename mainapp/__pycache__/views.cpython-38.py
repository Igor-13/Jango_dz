U
    ?*#c?  ?                   @   s?   d dl m Z  d dlmZ G dd? de?ZG dd? de?ZG dd? de?ZG d	d
? d
e?ZG dd? de?ZG dd? de?ZG dd? de?Z	dS )?    )?datetime)?TemplateViewc                   @   s   e Zd ZdZdS )?MainPageViewzmainapp/index.htmlN??__name__?
__module__?__qualname__?template_name? r
   r
   ?I   /home/igor/Рабочий стол/djangoBasics/Jango_dz/mainapp/views.pyr      s   r   c                       s    e Zd ZdZ? fdd?Z?  ZS )?NewsPageViewzmainapp/news.htmlc                    s:   t ? jf |?}d|d< d|d< td?|d< t?? |d< |S )Nu4   Громкий новостной заголовокZ
news_titleug   Предварительное описание, которое заинтересует каждогоZnews_preview?   ?rangeZdatetime_obj)?super?get_context_datar   r   ?now)?self?kwargs?context??	__class__r
   r   r      s    zNewsPageView.get_context_data)r   r   r   r	   r   ?__classcell__r
   r
   r   r   r   
   s   r   c                       s   e Zd Z? fdd?Z?  ZS )?NewsWithPaginatorViewc                    s"   t ? jf d|i|??}||d< |S )N?pageZpage_num)r   r   )r   r   r   r   r   r
   r   r      s    z&NewsWithPaginatorView.get_context_data)r   r   r   r   r   r
   r
   r   r   r      s   r   c                   @   s   e Zd ZdZdS )?CoursesPageViewzmainapp/courses_list.htmlNr   r
   r
   r
   r   r      s   r   c                   @   s   e Zd ZdZdS )?ContactsPageViewzmainapp/contacts.htmlNr   r
   r
   r
   r   r   #   s   r   c                   @   s   e Zd ZdZdS )?DocSitePageViewzmainapp/doc_site.htmlNr   r
   r
   r
   r   r   '   s   r   c                   @   s   e Zd ZdZdS )?LoginPageViewzmainapp/login.htmlNr   r
   r
   r
   r   r   +   s   r   N)
r   ?django.views.genericr   r   r   r   r   r   r   r   r
   r
   r
   r   ?<module>   s   