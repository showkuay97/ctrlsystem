from django.db import models

class repair_cmpt(models.Model):
    class_room = models.CharField(max_length=255) #ห้องเรียน
    name_aj = models.CharField(max_length=255)
    slug_repair = models.SlugField(max_length=255) #ห้องที่ซ่อม
    No_cmpt = models.CharField(max_length=2) #หมายเลขเครื่อง
    img_cmpt = models.CharField(max_length=255) #รุปเครื่อง
    stat_cmpt = models.CharField(max_length=255) #สถานะเครื่อง
    detail_repair = models.TextField() #รายละเอียดแจ้งซ่อม
    date_report = models.CharField(max_length=255) #วันแจ้งซ่อม
    date_input = models.CharField(max_length=255) #วันรับเครื่อง
    date_output = models.CharField(max_length=255) #วันส่งเครื่อง
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
    count_cpu = models.IntegerField(default=0)
    count_ram = models.IntegerField(default=0)
    count_hdd = models.IntegerField(default=0)
    count_ssd = models.IntegerField(default=0)
    count_psu = models.IntegerField(default=0)
    count_case = models.IntegerField(default=0)
    count_monitor = models.IntegerField(default=0)
    count_gpu = models.IntegerField(default=0)
    count_program = models.IntegerField(default=0)
    count_windows = models.IntegerField(default=0)
    count_all = models.IntegerField(default=0)
    count_power = models.IntegerField(default=0)
    count_board = models.IntegerField(default=0)
    count_lic  = models.IntegerField(default=0)
    count_keyboard = models.IntegerField(default=0)
    count_mouse = models.IntegerField(default=0)
    count_internet = models.IntegerField(default=0)
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

