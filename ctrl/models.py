from django.db import models

class repair_cmpt(models.Model):
    class_room = models.CharField(max_length=3)
    slug_repair = models.SlugField(max_length=255)
    No_cmpt = models.CharField(max_length=2)
    img_cmpt = models.ImageField()
    stat_cmpt = models.CharField(max_length=255)
    detail_repair = models.CharField(max_length=255)
    date_input = models.DateField(auto_now_add=True)
    date_output = models.DateField(auto_now_add=True)
    user_report = models.CharField(max_length=255)
    check_repair =models.CharField(max_length=255)
    repair = models.CharField(max_length=255)
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
    detail_repair = models.CharField(max_length=255)
    device_repair = models.CharField(max_length=255)
    def __str__(self):
        return self.slug_report