import requests
import dryscrape

first_page_url = 'https://www.dmv.ca.gov/wasapp/foa/findOfficeVisit.do'
second_page_url = 'https://www.dmv.ca.gov/wasapp/foa/reviewOfficeVisit.do'
third_page_url = 'https://www.dmv.ca.gov/wasapp/foa/confirmOfficeVisit.do'
# session = requests.session()

sess = dryscrape.Session()


def get_info(first_name, last_name, tel_area, tel_prefix, tel_suffix):
    # first_page_payload = {
    #     'officeId': 528,
    #     'numberItems': 1,
    #     'taskDl': True,
    #     'fdlNumber': None,
    #     'firstName': first_name,
    #     'lastName': last_name,
    #     'telArea': tel_area,
    #     'telPrefix': tel_prefix,
    #     'telSuffix': tel_suffix,
    #     'resetCheckFields': True,
    # }
    #
    # second_page_payload = {
    #     'chosenOfficeId': 0
    # }

    # r = session.post(first_page_url, data=first_page_payload, )
    sess.visit(first_page_url)
    office = sess.at_xpath('//*[@id="app_content"]/form/fieldset[1]//select')
    form = office.form()
    office.set(528)

    number_items = sess.at_xpath('//*[@id="one_task"]')
    number_items.click()

    reason_visit = sess.at_xpath('//*[@id="taskDL"]')
    reason_visit.click()

    first_name_elem = sess.at_xpath('//*[@id="first_name"]')
    first_name_elem.set(first_name)

    last_name_elem = sess.at_xpath('//*[@id="last_name"]')
    last_name_elem.set(last_name)

    tel_area_elem = sess.at_xpath('//*[@id="area_code"]')
    tel_area_elem.set(tel_area)
    tel_prefix_elem = sess.at_xpath('//*[@id="app_content"]/form/fieldset[4]/table/tbody/tr[6]/td[2]/input[2]')
    tel_prefix_elem.set(tel_prefix)
    tel_suffix_elem = sess.at_xpath('//*[@id="app_content"]/form/fieldset[4]/table/tbody/tr[6]/td[2]/input[3]')
    tel_suffix_elem.set(tel_suffix)

    form.submit()

    # print('cookies 1', requests.utils.dict_from_cookiejar(session.cookies))
    # r = session.post(second_page_url, data=second_page_payload)
    # print('cookies 2', requests.utils.dict_from_cookiejar(session.cookies))
    #
    # r = session.post(third_page_url)

    # print('cookies 2', requests.utils.dict_from_cookiejar(session.cookies))
    #
    # print(r.text)  # look for Your confirmation number is #span alert


get_info('test', 'abc', '123', '123', '1234')
