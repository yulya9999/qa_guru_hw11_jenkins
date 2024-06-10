from pages.registration_page import RegistrationPage


def test_user_can_send_form():
    registration_page = RegistrationPage()
    (
        (
            registration_page.open_browser()
            .fill_first_name('Yulia')
            .fill_last_name('Vdovina')
            .fill_email('yulya_vdovina@mail.ru')
            .fill_number('0123456789')
            .fill_address('Penza, st. Ladoga 1234')
            .fill_date_of_birth('11', '028', '2000')
            .fill_subject('Economics')
            .fill_gender('2')
            .fill_hobbies()
            .upload_file('kit.jpg')
            .fill_state('Haryana')
            .fill_city('Karnal')

            .submit()
            .registered_user_with(
                "Yulia Vdovina",
                "yulya_vdovina@mail.ru",
                "Female",
                "0123456789",
                "28 December,2000",
                "Economics",
                "Sports",
                "kit.jpg",
                "Penza, st. Ladoga 1234",
                "Haryana Karnal",
            )
        )
    )