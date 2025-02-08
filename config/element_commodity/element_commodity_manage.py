class Element_Commodity_Manage():
    """
    商品管理页面元素
    """
    commodity_button_element = ("xpath","//cite[text()='商品']")
    """商品"""

    commodity_manage_element = ("xpath","//cite[text()='商品管理']")
    """商品管理"""

    first_iframe = ("xpath","//iframe[@src='/admin/goods/lists.html']")
    """第一层iframe"""

    add_iframe = ("xpath","//iframe[@src='/admin/goods/add.html']")
    """新增层iframe"""

    edit_iframe = ("xpath","//iframe[@src='/admin/goods/edit.html?goods_id=10']")
    """编辑层iframe"""

    image_iframe = ("xpath","//iframe[@src='/admin/file/image.html']")
    """图片层iframe"""

    sale_commodity = ("xpath","//li[contains(text(),'销售中商品')]")
    """销售中商品"""

    warehouse_commodity = ("xpath","//li[contains(text(),'仓库中商品')]")
    """仓库中商品"""

    warehouse_alert_commodity = ("xpath","//li[contains(text(),'库存预警商品')]")
    """库存预警商品"""

    reclaim_commodity_element = ("xpath","//li[contains(text(),'回收站商品')]")
    """回收站商品"""

    inquire_commodity_name_element = ("xpath","//input[@id='keyword']")
    """查询-商品名称"""

    inquire_commodity_encode_element = ("xpath","//input[@id='code']")
    """查询-商品编码"""

    inquire_commodity_classify_element = ("xpath","//label[text()='商品分类:']/parent::*//input[@type='text']")
    """查询-商品分类"""

    inquire_commodity_suppliers_element = ("xpath","//label[text()='商品供货商:']/parent::*//input[@type='text']")
    """查询-商品供货商"""

    publish_commodity = ("xpath","//button[text()='发布商品']")
    """发布商品"""

    Takedown_commodity = ("xpath","//button[@id='lower']")
    """下架"""

    Shelves_commodity = ("xpath","//button[@id='upper']")
    """上架"""

    commodity_name = ("xpath","//input[@name='name']")
    """商品名称"""

    commodity_encode = ("xpath","//input[@name='code']")
    """商品编码"""

    first_commodity_classify = ("xpath","//div[@class='layui-form-item']//label[contains(text(),'商品分类')]/following-sibling::div[1]//input")
    """第一层商品分类"""

    second_commodity_classify = ("xpath","//div[@class='layui-form-item']//label[contains(text(),'商品分类')]/following-sibling::div[2]//input")
    """第二层商品分类"""

    third_commodity_classify = ("xpath","//div[@class='layui-form-item']//label[contains(text(),'商品分类')]/following-sibling::div[3]//input")
    """第三层商品分类"""

    commodity_peculiarity = ("xpath","//input[@name='remark']")
    """商品卖点"""

    commodity_main_image = ("xpath","//div[@class='goods-img-add goods-image upload-image-div']//a[@class='upload-image-a'][contains(text(),'+ 添加图片')]")
    """商品主图"""

    commodity_revolve_image = ("xpath","//div[@class='goods-img-add upload-image-div']//a[@class='upload-image-a'][contains(text(),'+ 添加图片')]")
    """商品轮播图"""

    commodity_video = ("xpath","//a[@class='upload-file-title']")
    """商品视频"""

    custom_posters = ("xpath","//div[@class='goods-img-add poster-upload upload-image-div']//a[@class='upload-image-a'][contains(text(),'+ 添加图片')]")
    """自定义分享海报"""

    suppliers = ("xpath","//select[@name='brand_id']")
    """商品品牌"""


