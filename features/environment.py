def before_all(context):
    pass

def after_all(context):
    pass

def before_feature(context, feature):
    pass

def after_feature(context, feature):
    pass

def before_scenario(context, scenario):
    pass

def after_scenario(context, scenario):
    if hasattr(context, 'driver'):
        try:
            context.driver.quit()
        except:
            pass