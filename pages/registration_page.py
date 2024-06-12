from selene import browser, have, command
from pathlib import Path
import tests
import allure


class RegistrationPage:
    def __init__(self):
        self.state = browser.element('#state')
        self.city = browser.element('#city')

    @allure.step("Открытие страницы /automation-practice-form")
    def open_browser(self):
        browser.open("/automation-practice-form")
        return self

    @allure.step('Заполнение поля "First Name"')
    def fill_first_name(self, value):
        browser.element("#firstName").type(value)
        return self

    @allure.step('Заполнение поля "Last Name"')
    def fill_last_name(self, value):
        browser.element("#lastName").type(value)
        return self

    @allure.step('Заполнение поля "Email"')
    def fill_email(self, value):
        browser.element("#userEmail").type(value)
        return self

    @allure.step('Заполнение поля "Mobile"')
    def fill_number(self, value):
        browser.element("#userNumber").type(value)
        return self

    @allure.step('Заполнение поля "Current Address"')
    def fill_address(self, value):
        browser.element("#currentAddress").type(value)
        return self

    @allure.step('Установка даты "Date of Birth"')
    def fill_date_of_birth(self, month, day, year):
        browser.element("#dateOfBirthInput").click()
        browser.element(f'.react-datepicker__month-select option[value="{month}"]').click()
        browser.element(f'.react-datepicker__year-select option[value="{year}"]').click()
        browser.all(f'.react-datepicker__day--{day}').second.click()
        return self

    @allure.step('Заполнение поля "Subjects"')
    def fill_subject(self, value):
        browser.element("#subjectsInput").type(f"{value}")
        browser.element(".subjects-auto-complete__menu").click()
        browser.element("#subjectsInput").type(f"{value}").press_tab()

        return self

    @allure.step('Установка радиокнопки в поле "Gender"')
    def fill_gender(self, value):
        browser.element(f'[for="gender-radio-{value}"]').click()
        return self

    @allure.step('Установка чекбокса в поле "Hobbies"')
    def fill_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()
        return self

    @allure.step('Загрузка изображения. Поле "Picture"')
    def upload_file(self, file_name):
        browser.element('#uploadPicture').type(
            str(Path(tests.__file__).parent.joinpath(f'data/{file_name}'))
        )
        return self

    @allure.step('Выбор из выпадающего списка "State"')
    def fill_state(self, value):
        self.state.perform(command.js.scroll_into_view).click()
        self.state.all('[id^=react-select-3-option]').element_by(
            have.text(value)
        ).click()

        return self

    @allure.step('Выбор из выпадающего списка "City"')
    def fill_city(self, value):
        self.city.click()
        self.city.all('[id^=react-select-4-option]').element_by(
            have.text(value)
        ).click()

        return self

    @allure.step('Отправка формы. Кнопка "Submit"')
    def submit(self):
        browser.element("#submit").click()
        return self

    def registered_user_with(self, full_name, email, gender, phone, date, subject, hobbies, file, address,
                             state):
        browser.element(".modal-content").element("table").all("tr").all("td").even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                date,
                subject,
                hobbies,
                file,
                address,
                state,
            )
        )
