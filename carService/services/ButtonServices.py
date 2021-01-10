from carService.models.ServiceButtonObject import ServiceButtonObject


def get_buttons(group_name: str, service_situation: str):
    buttons = []

    button_object_info = ServiceButtonObject()
    button_object_info.buttonName = 'İşlem Bilgi'
    button_object_info.buttonFunction = 'goServiceDetail'

    button_object_confirm = ServiceButtonObject()
    button_object_confirm.buttonName = 'Onayla'
    button_object_confirm.buttonFunction = 'goServiceApprove'

    button_object_make_determination = ServiceButtonObject()
    button_object_make_determination.buttonName = 'Arıza Tespiti Yap'
    button_object_make_determination.buttonFunction = 'goServiceDetermination'

    button_object_get_process = ServiceButtonObject()
    button_object_get_process.buttonName = 'İşleme Al'
    button_object_get_process.buttonFunction = 'serviceGetProcess'

    button_object_complete_process = ServiceButtonObject()
    button_object_complete_process.buttonName = 'İşlem Tamamla'
    button_object_complete_process.buttonFunction = 'serviceProcessComplete'

    button_object_deliver = ServiceButtonObject()
    button_object_deliver.buttonName = 'Teslim Et'
    button_object_deliver.buttonFunction = 'serviceDeliver'

    if group_name == 'Admin':

        if service_situation == 'Arıza Tespiti Bekleniyor':
            buttons.append(button_object_info)

        elif service_situation == 'Müşteri Onayı Bekleniyor':
            buttons.append(button_object_info)
            buttons.append(button_object_confirm)

        elif service_situation == 'İşlem Bekleniyor':
            buttons.append(button_object_info)

        elif service_situation == 'İşlemde':
            buttons.append(button_object_info)

        elif service_situation == 'Tamamlandı':
            buttons.append(button_object_info)
            buttons.append(button_object_deliver)
        else:
            buttons.append(button_object_info)

    elif group_name == 'Tamirci':

        if service_situation == 'Arıza Tespiti Bekleniyor':
            buttons.append(button_object_info)
            buttons.append(button_object_make_determination)

        elif service_situation == 'Müşteri Onayı Bekleniyor':
            buttons.append(button_object_info)

        elif service_situation == 'İşlem Bekleniyor':
            buttons.append(button_object_info)
            buttons.append(button_object_get_process)

        elif service_situation == 'İşlemde':
            buttons.append(button_object_info)
            buttons.append(button_object_complete_process)

        elif service_situation == 'Tamamlandı':
            buttons.append(button_object_info)

        else:
            buttons.append(button_object_info)

    elif group_name == 'Customer':
        if service_situation == 'Arıza Tespiti Bekleniyor':
            buttons.append(button_object_info)

        elif service_situation == 'Müşteri Onayı Bekleniyor':
            buttons.append(button_object_info)
            buttons.append(button_object_confirm)

        else:
            buttons.append(button_object_info)

    else:
        buttons.append(button_object_info)

    return buttons


def get_buttons_payment(payment_situation: str):
    buttons = []

    button_object_info = ServiceButtonObject()
    button_object_info.buttonName = 'İşlem Bilgi'
    button_object_info.buttonFunction = 'getPaymentMovementsList'

    button_object_payment = ServiceButtonObject()
    button_object_payment.buttonName = 'Ödeme Yap'
    button_object_payment.buttonFunction = 'makePayment'
    if payment_situation == 'Ödendi':
        buttons.append(button_object_info)

    else:
        buttons.append(button_object_info)
        buttons.append(button_object_payment)

    return buttons
