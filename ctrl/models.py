from django.db import models

class repair_cmpt(models.Model):
    class_room = models.CharField(max_length=3) #ห้องเรียน
    slug_repair = models.SlugField(max_length=255) #ห้องที่ซ่อม
    No_cmpt = models.CharField(max_length=2) #หมายเลขเครื่อง
    img_cmpt = models.CharField(max_length=255) #รุปเครื่อง
    stat_cmpt = models.CharField(max_length=255) #สถานะเครื่อง
    detail_repair = models.TextField() #รายละเอียดแจ้งซ่อม
    date_input = models.DateField(auto_now_add=True) #วันรับเครื่อง
    date_output = models.DateField(auto_now_add=True) #วันส่งเครื่อง
    user_report = models.CharField(max_length=255) #คนที่แจ้ง
    check_repair =models.TextField() #สาเหตุเครื่องเสีย
    repair = models.TextField() #สรุปการซ่อม
    def __str__(self):
        return self.slug_repair

class cmpt_detail(models.Model):
    class_room = models.CharField(max_length=255)
    slug_detail = models.SlugField(max_length=255)
    No_cmpt = models.CharField(max_length=2)
    board = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    hdd = models.CharField(max_length=255)
    ssd = models.CharField(max_length=255)
    psu = models.CharField(max_length=255)
    case = models.CharField(max_length=255)
    monitor = models.CharField(max_length=255)
    gpu = models.CharField(max_length=255)
    count_cpu = models.CharField(max_length=255)
    count_ram = models.CharField(max_length=255)
    count_hdd = models.CharField(max_length=255)
    count_ssd = models.CharField(max_length=255)
    count_psu = models.CharField(max_length=255)
    count_case = models.CharField(max_length=255)
    count_monitor = models.CharField(max_length=255)
    count_gpu = models.CharField(max_length=255)
    count_all = models.IntegerField()
    def __str__(self):
        return self.slug_detail

class report(models.Model):
    class_room = models.CharField(max_length=255)
    slug_report = models.SlugField(max_length=255)
    No_cmpt = models.CharField(max_length=2)
    detail_repair = models.TextField()
    device_repair = models.TextField()
    def __str__(self):
        return self.slug_report

class options_std(models.Model):
    class_room = models.CharField(max_length=3)
    slug_class_room = models.SlugField(max_length=3)

    def __str__(self):
        return self.slug_class_room

class options_tcher(models.Model):
    room =models.CharField(max_length=255)
    slug_room =  models.SlugField(max_length=255)

    def __str__(self):
        return self.slug_room
    