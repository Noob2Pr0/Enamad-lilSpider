# Enamad-lilSpider
اسکریپت خزنده وب اینماد جهت جمع آوری بانک اطلاعاتی ایمیل و تلفن کسب کار های مختلف | Enamad.ir web crawler script to collect email and phone database of different businesses

**نحوه استفاده از ابزار را در آخر این متن حتما بخوانید**

# مهم
 **این ابزار کوچک به جهت مصارف تبلیغاتی تولید شده است به همین دلیل هر گونه مسئولیت استفاده از این اسکریپت و اطلاعات به عهده مصرف کننده می باشد
همچنین در صورتی که اطلاعات شما در این بانک اطلاعاتی بوده و تمایلی به اشتراک گذاشته شدن آن ندارید به ایمیل omidnasiri.p@gmail.com پیام داده تا در اولین فرصت اطلاعات شما از بانک اطلاعاتی حذف گردید**

_فعالیت این خزنده قانونی می باشد زیرا تنها وب سایت هایی که در سایت اینماد ثبت نام کرده اند و خودشان اطلاعاتشان را به اشتراک گذاشته اند را جمع آوری می کند._

شما می توانید بصورت مستقیم این بانک اطلاعاتی را که با نام **full-enamad-db.rar** مشخص شده است را دانلود کنید
همچنین با توجه به این که قصد بروز رسانی این ابزار را تا مدت های طولانی ندارم در صورت قدیمی شدن بانک اطلاعاتی می توانید از اسکریپت جهت استخراج اطلاعات مجوز داران استفاده نمایید

**این بانک اطلاعاتی به مقدار 217857 نفر و حجم 25 مگابایت که آخرین بروز رسانی آن تاریخ 27 اردیبهشت 1403 می باشد**

# important
**This small tool has been produced for advertising purposes, therefore any responsibility for using this script and information is the responsibility of the consumer.
Also, if your information is in this database and you do not want it to be shared, send a message to the email (omidnasiri.p@gmail.com) so that your information is removed from the database as soon as possible.**

_The activity of this crawler is legal because it collects only the websites that have registered on the Inmad site and shared their information themselves._

You can directly download this database named **full-enamad-db.rar**
Also, due to the fact that I do not intend to update this tool for a long time, if the database becomes old, you can use the script to extract the license holders' information.

**This database has a volume of 7 and a volume of 8, the last update of which is the date of 5/16/2024**


# نحوه استفاده از ابزار
میدونم کد افتضاح نوشته شده ولی چون برای استفاده عموم ننوشته بودم بلکه برای مصرف شخصی بود گذاشتم تا بعدا به مرور زمان بهبودش بدم
سیستم عاملی که باید روش اجرا کنید حتما باید لینوکس باشه چون دستورات سیستم عاملی os و grep, cut استفاده شده توش
تا در آینده بیام کدی رو جایگذینش کنم برای مصارف همه سیستم عامل ها
ابزار های curl , grep , cut از پیش نصب شده باشن، مهم نیست لینوکستون تو ماشین مجازی باشه یا از از wsl استفاده کرده باشید و...
عدد 7251 رو به 3 تغییر بدید یک بار اجرا کنید عملکرد ابزار رو تست کنید و بعد 7251 رو قرار بدید برای استخراج 217000 لینک
خودش بصورت خودکار همه کار هار و انجام میده و فایل نهایی enamad-data.txt ذخیره میشه که کافیه با excel بازش کنی یا استفاده های دیگه خلاقانه تری باهاش انجام بدی
من از مودم خونه انجام دادم ولی پیشنهاد میکنم سرور ایران داشته باشی چون به ip ایران محدوده سایت enamad.ir
اگه خواستی سرعت ببخشی میتونی فایل extracted_urls.txt رو اسمشو به enamad-URLS.txt تغییر بدی و در آخر کد ابزار get_links رو کامنت کنی تا در وقت صرفه جویی بشه
امید وارم به کارت بیاد و لذتشو ببری



# How to use the tool
I know that the code is written badly, but because I did not write it for public use, it's for personal use, I left it to improve it later over time.
The operating system you need to run must be Linux because the operating system commands os, grep, cut are used in it
In the future, I will replace the code for the use of all operating systems
curl, grep, cut tools are pre-installed, it doesn't matter if your Linux is in a virtual machine or used wsl and...
Change the number 7251 to 3, run it once, test the function of the tool, and then enter 7251 to extract 217,000 links.
It does all the work automatically and the final file enamad-data.txt is saved, you just need to open it with excel or do other creative uses with it.
I did it from my home modem, but I suggest that you have an Iranian server, because the enamad.ir site response just iran ip
If you want to speed it up, you can rename the extracted_urls.txt file to enamad-URLS.txt and comment the **get_links** tool code at the end to save time.
I hope it comes to you and you enjoy it
