
class Element_Supplier():
    """
    供货商页面元素
    """
    commodity_button_element = ("xpath", "//cite[text()='商品']")
    """菜单栏商品"""

    supplise_button_elment = ('xpath', "//cite[contains(text(),'供货商')]")
    """供货商"""

    first_iframe = ('xpath', "//iframe[@src='/admin/supplier/lists.html']")
    """第一层iframe"""

    second_iframe = ('xpath', "//iframe[@src='/admin/supplier/add.html']")
    """第二层iframe"""

    revise_iframe = ('xpath', "//div[@class='layui-layer-title']/following-sibling::div/iframe")
    """修改层iframe"""

    add_supplise_button_elment = ('xpath', "//button[text()='新增供货商']")
    """新增供货商"""

    supplise_inquire_input = ('xpath', "//input[@id='keyword']")    #
    """供货商查询输入框"""

    add_name_input = ('xpath', "//input[@name='name']")     #
    """新增-供货商名称输入框"""

    add_contact_input = ('xpath', "//input[@name='contact']")   #
    """新增-联系人姓名输入框"""

    add_tel_input = ('xpath', "//input[@name='tel']")
    """新增-联系电话输入框"""

    add_address_input = ('xpath', "//input[@name='address']")
    """新增-联系地址输入框"""

    add_remark_input1 = ('xpath', "//textarea[@name='remark3']")
    """新增-备注输入框"""

    add_remark_input = ('xpath', "//textarea[@name='remark']")
    """新增-备注输入框"""

    verify_add_elment = ('xpath', "//div[text()='测试供应商']")
    """ 测试供应商"""

    add_pop_ups_title = ('xpath', "//div[text()='新增供货商']")
    """新增弹窗标题"""

    add_supliers_window = ('xpath', "//div[@class='layui-layer-title' and text()='新增供货商']")
    """新增供货商弹窗"""
