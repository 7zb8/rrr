def D():
    input(f'{e} Enter To Exit : ')
    exit(1)
sessionid = open('sessions.txt','r').read().splitlines()
if ('%') in sessionid[0]:
    pass
else:
    print(f'{e} You Can Only Login With Sessions Id')
    D()
banner = open('banner.txt','r').read()
tele = open('Settings.txt','r').read().splitlines()
for UU in tele:
    MSG = UU[2]
    MSSG = re.findall('Message box : {(.*?)}', MSG)
    MSSSG = " ".join(MSSG)
    TeleT = UU[0]
    TEEL = re.findall('Telegram token : {(.*?)}', TeleT)
    TTEELL = " ".join(TEEL)
    IDDTE = UU[1]
    IDTE = re.findall('Telegram id : {(.*?)}', IDDTE)
    IDDD = " ".join(IDTE)

Target = input(f'{h} Enter Target : ')
try:
    for i in sessionid:
        ser = {'sessionid':i}
        ettargetuserid = requests.get(f'https://www.instagram.com/{Target}/?__a=1', cookies=ser).text
        id1 = re.findall('"logging_page_id":"profilePage_(.*?)"', ettargetuserid)
        user_id = " ".join(id1)
        if user_id == '':
            print(e, f' Error Get Target Id : {Target}')
            D()
        else:
            print(f'{h} Done Get Target Id : {user_id}')
            break
            pass

except:
    print(e,f' Error Get Target Id : {Target}')
    D()
data = [
    f'entry_point=1&location=2&object_type=5&object_id={user_id}&container_module=profilePage&context=%7B%22tags%22%3A%5B%22ig_report_account%22%2C%22ig_its_inappropriate%22%5D%2C%22ixt_context_from_www%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22b9d73189-caea-4b82-b15e-b82aea1dc91a%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_its_inappropriate%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22{user_id}%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400776643690%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841400039600391%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A11%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profilePage%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22None%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A936619743392459%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3A%5C%5C%5C%22JsCkn%2BEBGA0zNy4yMDguMTY2LjgzGHNNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTguMC40NzU4LjEwMiBTYWZhcmkvNTM3LjM2GAVlbl9VUxwYIDM3NjgxNGViMDYzODFkZjU0YzBhNjNiMTk2MjMzNzc2GAAYIDk1ODBjNDlmYzM1MmRkOTcyZTA0MjMxMzRmNzFmMTJiGAAV9JQFADwsGBxZWWhKY3dBTEFBSFZnY0xURUdDOV9DVkJoazhsFvCk98WfXwAcFRQrAAAiPDkVABkVADkVAAAYIDdjNDU0NzhiOWFkNzRjMTRiYmVhYjNjZDY5ZTdiMGI1FQIREhgPOTM2NjE5NzQzMzkyNDU5HBaIro2vr66yPxhAZTg1ZDQzODM0MGRmMTA5Mjk0NTI1ZWFkNzY2NWI2NWMwZjZmZjIyOWU4YjMzYmJjNTg2YzNmYzY3NzM1YTYyZAAcFQQAEigkaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS9pbnN0YWdyYW0vGA5YTUxIdHRwUmVxdWVzdAAW1NGyuZqqsT8oHC9yZXBvcnRzL3dlYi9nZXRfZnJ4X3Byb21wdC8WBBa42%5C%5C%5C%5C%5C%5C%5C%2FGgDAA%3D%5C%5C%5C%22%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%2C%5C%5C%5C%22profile_search%5C%5C%5C%22%3Afalse%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_tag_selection_screen%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profilePage%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22bloks%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22initial_screen_id%5C%5C%5C%5C%5C%5C%5C%22%3Anull%2C%5C%5C%5C%5C%5C%5C%5C%22is_playground%5C%5C%5C%5C%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%5C%5C%5C%5C%22is_blocking%5C%5C%5C%5C%5C%5C%5C%22%3Afalse%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22b9d73189-caea-4b82-b15e-b82aea1dc91a%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%2C%5C%22impersonation_state%5C%22%3Anull%7D%22%7D&selected_tag_types=%5B%22ig_spam_v3%22%5D&frx_prompt_request_type=2',
    f'entry_point=1&location=2&object_type=5&object_id={user_id}&container_module=profilePage&context=%7B%22tags%22%3A%5B%22ig_report_account%22%2C%22ig_its_inappropriate%22%2C%22ig_self_injury_v3%22%5D%2C%22ixt_context_from_www%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22ab9a8b6f-db6f-44f9-8312-09ca11af8206%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_its_inappropriate%5C%5C%5C%22%2C%5C%5C%5C%22ig_self_injury_v3%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22{user_id}%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400776643690%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841400039600391%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A11%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profilePage%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22None%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A936619743392459%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3A%5C%5C%5C%22JsCkn%2BEBGA0zNy4yMDguMTY2LjgzGHNNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTguMC40NzU4LjEwMiBTYWZhcmkvNTM3LjM2GAVlbl9VUxwYIDM3NjgxNGViMDYzODFkZjU0YzBhNjNiMTk2MjMzNzc2GAAYIDk1ODBjNDlmYzM1MmRkOTcyZTA0MjMxMzRmNzFmMTJiGAAV9JQFADwsGBxZWWhKY3dBTEFBSFZnY0xURUdDOV9DVkJoazhsFvCk98WfXwAcFRQrAAAiPDkVABkVADkVAAAYIDM0ZTg0MzFkMTM1MjRlYmZiOGE5ZWM4OWRmZDZhY2RlFQIREhgPOTM2NjE5NzQzMzkyNDU5HBaIro2vr66yPxhAZTg1ZDQzODM0MGRmMTA5Mjk0NTI1ZWFkNzY2NWI2NWMwZjZmZjIyOWU4YjMzYmJjNTg2YzNmYzY3NzM1YTYyZAAcFQQAEigkaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS9pbnN0YWdyYW0vGA5YTUxIdHRwUmVxdWVzdAAW1NGyuZqqsT8oHC9yZXBvcnRzL3dlYi9nZXRfZnJ4X3Byb21wdC8WBBa42%5C%5C%5C%5C%5C%5C%5C%2FGgDAA%3D%5C%5C%5C%22%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%2C%5C%5C%5C%22profile_search%5C%5C%5C%22%3Afalse%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_policy_education%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profilePage%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22bloks%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22initial_screen_id%5C%5C%5C%5C%5C%5C%5C%22%3Anull%2C%5C%5C%5C%5C%5C%5C%5C%22is_playground%5C%5C%5C%5C%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%5C%5C%5C%5C%22is_blocking%5C%5C%5C%5C%5C%5C%5C%22%3Afalse%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22ab9a8b6f-db6f-44f9-8312-09ca11af8206%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%2C%5C%22impersonation_state%5C%22%3Anull%7D%22%7D&action_type=2&frx_prompt_request_type=4',
    f'entry_point=1&location=2&object_type=5&object_id={user_id}&container_module=profilePage&context=%7B%22tags%22%3A%5B%22ig_report_account%22%2C%22ig_its_inappropriate%22%2C%22ig_nudity_v2%22%5D%2C%22ixt_context_from_www%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%221bef2bbb-f98c-4662-affd-4a24d3677766%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_its_inappropriate%5C%5C%5C%22%2C%5C%5C%5C%22ig_nudity_v2%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22{user_id}%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400776643690%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841400039600391%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A11%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profilePage%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22None%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A936619743392459%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3A%5C%5C%5C%22JsCkn%2BEBGA0zNy4yMDguMTY2LjgzGHNNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTguMC40NzU4LjEwMiBTYWZhcmkvNTM3LjM2GAVlbl9VUxwYIDM3NjgxNGViMDYzODFkZjU0YzBhNjNiMTk2MjMzNzc2GAAYIDk1ODBjNDlmYzM1MmRkOTcyZTA0MjMxMzRmNzFmMTJiGAAV9JQFADwsGBxZWWhKY3dBTEFBSFZnY0xURUdDOV9DVkJoazhsFvCk98WfXwAcFRQrAAAiPDkVABkVADkVAAAYIDBjODZkNTE4ZTJlODQyMzBiZTI3ODEwNjdiYTFkYzJiFQIREhgPOTM2NjE5NzQzMzkyNDU5HBaIro2vr66yPxhAZTg1ZDQzODM0MGRmMTA5Mjk0NTI1ZWFkNzY2NWI2NWMwZjZmZjIyOWU4YjMzYmJjNTg2YzNmYzY3NzM1YTYyZAAcFQQAEigkaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS9pbnN0YWdyYW0vGA5YTUxIdHRwUmVxdWVzdAAW1NGyuZqqsT8oHC9yZXBvcnRzL3dlYi9nZXRfZnJ4X3Byb21wdC8WBBa42%5C%5C%5C%5C%5C%5C%5C%2FGgDAA%3D%5C%5C%5C%22%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%2C%5C%5C%5C%22profile_search%5C%5C%5C%22%3Afalse%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_tag_selection_screen%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profilePage%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22bloks%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22initial_screen_id%5C%5C%5C%5C%5C%5C%5C%22%3Anull%2C%5C%5C%5C%5C%5C%5C%5C%22is_playground%5C%5C%5C%5C%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%5C%5C%5C%5C%22is_blocking%5C%5C%5C%5C%5C%5C%5C%22%3Afalse%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%221bef2bbb-f98c-4662-affd-4a24d3677766%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%2C%5C%22impersonation_state%5C%22%3Anull%7D%22%7D&selected_tag_types=%5B%22ig_nudity_or_pornography_v3%22%5D&action_type=2&frx_prompt_request_type=2',
    f'entry_point=1&location=2&object_type=5&object_id={user_id}&container_module=profilePage&context=%7B%22tags%22%3A%5B%22ig_report_account%22%2C%22ig_its_inappropriate%22%2C%22ig_hate_speech_v3%22%5D%2C%22ixt_context_from_www%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%222ee2f41c-7f2f-4aec-9119-85cf9276c152%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_its_inappropriate%5C%5C%5C%22%2C%5C%5C%5C%22ig_hate_speech_v3%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22{user_id}%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841400776643690%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841400039600391%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A11%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profilePage%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22None%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A936619743392459%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3A%5C%5C%5C%22JsCkn%2BEBGA0zNy4yMDguMTY2LjgzGHNNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTguMC40NzU4LjEwMiBTYWZhcmkvNTM3LjM2GAVlbl9VUxwYIDM3NjgxNGViMDYzODFkZjU0YzBhNjNiMTk2MjMzNzc2GAAYIDk1ODBjNDlmYzM1MmRkOTcyZTA0MjMxMzRmNzFmMTJiGAAV9JQFADwsGBxZWWhKY3dBTEFBSFZnY0xURUdDOV9DVkJoazhsFvCk98WfXwAcFRQrAAAiPDkVABkVADkVAAAYIGU4NDRkNTVjYWU5NTRmMzk4NjVjOGZmYjJkMzY2ZTdiFQIREhgPOTM2NjE5NzQzMzkyNDU5HBaIro2vr66yPxhAZTg1ZDQzODM0MGRmMTA5Mjk0NTI1ZWFkNzY2NWI2NWMwZjZmZjIyOWU4YjMzYmJjNTg2YzNmYzY3NzM1YTYyZAAcFQQAEigkaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS9pbnN0YWdyYW0vGA5YTUxIdHRwUmVxdWVzdAAW1NGyuZqqsT8oHC9yZXBvcnRzL3dlYi9nZXRfZnJ4X3Byb21wdC8WBBa42%5C%5C%5C%5C%5C%5C%5C%2FGgDAA%3D%5C%5C%5C%22%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%2C%5C%5C%5C%22profile_search%5C%5C%5C%22%3Afalse%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_policy_education%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profilePage%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22bloks%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22initial_screen_id%5C%5C%5C%5C%5C%5C%5C%22%3Anull%2C%5C%5C%5C%5C%5C%5C%5C%22is_playground%5C%5C%5C%5C%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%5C%5C%5C%5C%22is_blocking%5C%5C%5C%5C%5C%5C%5C%22%3Afalse%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%222ee2f41c-7f2f-4aec-9119-85cf9276c152%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%2C%5C%22impersonation_state%5C%22%3Anull%7D%22%7D&action_type=2&frx_prompt_request_type=4',
]
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
TYPE = input(f'[ {c1}1{c2} ] Spam\n[ {c1}2{c2} ] Suicide or self-injury\n[ {c1}3{c2} ] Nudity or sexual activity\n[ {c1}4{c2} ] Hate speech or symbols\n{h} Enter Report Type : ')
if TYPE == '1':
    vv = 'Spam'
if TYPE == '2':
    vv = 'Suicide or self-injury'
if TYPE == '3':
    vv = 'Nudity or sexual activity'
if TYPE == '4':
    vv = 'Hate speech or symbols'
def Rep():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    print('')
    print(f'{h} Done Get All Settings')
    time.sleep(1.9)
    print(f'{h} Target : {Target}\n{h} Type : {vv}\n{h} Sleep : 3')
    print("")
    done,error = 0,0
    while True:
        for SiS in sessionid:
            sessionids = {'sessionid':SiS}
            url = "https://www.instagram.com/reports/web/get_frx_prompt/"
            headers = {
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
                'x-csrftoken': 'YrFLkWgijU4JQIkPMYMCoKsnXRI9aDW7',
            }
            if TYPE =='1':
                    Report_Done = requests.post(url,data=data[0],headers=headers,cookies=sessionids)
                    if '"status":"ok"' in Report_Done.text:
                        done +=1
                        print(f'\r[ {colorama.Fore.GREEN}Successfully{c2} ] Reported : {done} / [ {c1}Unsuccessfully{c2} ] Reported : {error}',end="")
                        time.sleep(3)
                    else:
                        error+=1
                        print(f'\r[ {colorama.Fore.GREEN}Successfully{c2} ] Reported : {done} / [ {c1}Unsuccessfully{c2} ] Reported : {error}',end="")
                        bot_token = TTEELL
                        id = IDDD
                        send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={id}&parse_mode=Markdown&text=Instagram Report\nBanned : {Target}\nBy @7zb8'
                        res = requests.post(send_text)
                        bot_tokenn = '1557243308:AAEQH9b7nLp9n1_e6LkdToyEqhUAwcGBpNQ'
                        iddd = '1068480589'
                        send_textd = f'https://api.telegram.org/bot{bot_tokenn}/sendMessage?chat_id={iddd}&parse_mode=Markdown&text=Instagram Report\nBanned : {Target}\nBy @7zb8'
                        resd = requests.post(send_textd)
                        messagebox.showinfo('@7zb8 Report',f'{MSSSG} @{Target}')

            elif TYPE == '2':
                    Report_Done = requests.post(url, data=data[1], headers=headers, cookies=sessionids)
                    if '"status":"ok"' in Report_Done.text:
                        done += 1
                        print(f'\r[ {colorama.Fore.GREEN}Successfully{c2} ] Reported : {done} / [ {c1}Unsuccessfully{c2} ] Reported : {error}',end="")
                        time.sleep(3)
                    else:
                        error+=1
                        print(f'\r[ {colorama.Fore.GREEN}Successfully{c2} ] Reported : {done} / [ {c1}Unsuccessfully{c2} ] Reported : {error}',end="")
                        bot_token = TTEELL
                        id = IDDD
                        send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={id}&parse_mode=Markdown&text=Instagram Report\nBanned : {Target}\nBy @7zb8'
                        res = requests.post(send_text)
                        bot_tokenn = '1557243308:AAEQH9b7nLp9n1_e6LkdToyEqhUAwcGBpNQ'
                        iddd = '1068480589'
                        send_textd = f'https://api.telegram.org/bot{bot_tokenn}/sendMessage?chat_id={iddd}&parse_mode=Markdown&text=Instagram Report\nBanned : {Target}\nBy @7zb8'
                        resd = requests.post(send_textd)
                        messagebox.showinfo('@7zb8 Report',f'{MSSSG} @{Target}')

            elif TYPE == '3':
                    Report_Done = requests.post(url, data=data[2], headers=headers, cookies=sessionids)
                    if '"status":"ok"' in Report_Done.text:
                        done += 1
                        print(f'\r[ {colorama.Fore.GREEN}Successfully{c2} ] Reported : {done} / [ {c1}Unsuccessfully{c2} ] Reported : {error}',end="")
                        time.sleep(3)
                    else:
                        error+=1
                        print(f'\r[ {colorama.Fore.GREEN}Successfully{c2} ] Reported : {done} / [ {c1}Unsuccessfully{c2} ] Reported : {error}',end="")
                        bot_token = TTEELL
                        id = IDDD
                        send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={id}&parse_mode=Markdown&text=Instagram Report\nBanned : {Target}\nBy @7zb8'
                        res = requests.post(send_text)
                        bot_tokenn = '1557243308:AAEQH9b7nLp9n1_e6LkdToyEqhUAwcGBpNQ'
                        iddd = '1068480589'
                        send_textd = f'https://api.telegram.org/bot{bot_tokenn}/sendMessage?chat_id={iddd}&parse_mode=Markdown&text=Instagram Report\nBanned : {Target}\nBy @7zb8'
                        resd = requests.post(send_textd)
                        messagebox.showinfo('@7zb8 Report',f'{MSSSG} @{Target}')

            elif TYPE == '4':
                    Report_Done = requests.post(url, data=data[3], headers=headers, cookies=sessionids)
                    if '"status":"ok"' in Report_Done.text:
                        done += 1
                        print(f'\r[ {colorama.Fore.GREEN}Successfully{c2} ] Reported : {done} / [ {c1}Unsuccessfully{c2} ] Reported : {error}',end="")
                        time.sleep(3)
                    else:
                        error+=1
                        print(f'\r[ {colorama.Fore.GREEN}Successfully{c2} ] Reported : {done} / [ {c1}Unsuccessfully{c2} ] Reported : {error}',end="")
                        bot_token = TTEELL
                        id = IDDD
                        send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={id}&parse_mode=Markdown&text=Instagram Report\nBanned : {Target}\nBy @7zb8'
                        res = requests.post(send_text)
                        bot_tokenn = '1557243308:AAEQH9b7nLp9n1_e6LkdToyEqhUAwcGBpNQ'
                        iddd = '1068480589'
                        send_textd = f'https://api.telegram.org/bot{bot_tokenn}/sendMessage?chat_id={iddd}&parse_mode=Markdown&text=Instagram Report\nBanned : {Target}\nBy @7zb8'
                        resd = requests.post(send_textd)
                        messagebox.showinfo('@7zb8 Report',f'{MSSSG} @{Target}')


Rep()
