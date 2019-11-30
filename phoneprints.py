#program runs web services to track phone number

import webbrowser

areaCode = input("What is the area code of the phone number? ")
middle3 = input("What are the middle 3 digits? ")
last4 = input("What are the last 4 digits? ")

phoneNumber = str(areaCode) + str(middle3) + str(last4)

fourOneOne = "https://www.411.com/phone/" + "1-" + str(areaCode) + "-" + str(middle3) + "-" + str(last4)
webbrowser.open(fourOneOne)

spyTox = "https://www.spytox.com/people/search?phone=" + str(areaCode) + "-" + str(middle3) + "-" + str(last4)
webbrowser.open(spyTox)

fastPeopleSearch = "https://www.fastpeoplesearch.com/" + str(areaCode) + "-" + str(middle3) + "-" + str(last4)
webbrowser.open(fastPeopleSearch)

truePeopleSearch = "https://www.truepeoplesearch.com/results?phoneno=" + "(" + str(areaCode) + ")" + str(middle3) + "-" + str(last4)
webbrowser.open(truePeopleSearch)

phoneLookUp = "https://www.phonelookup.com/" + "1/" + str(areaCode) + "-" + str(middle3) + "-" + str(last4)
webbrowser.open(phoneLookUp)

usPhoneBook = "https://www.usphonebook.com/" + str(areaCode) + "-" + str(middle3) + "-" + str(last4)
webbrowser.open(usPhoneBook)

thatsThem = "https://thatsthem.com/phone/" + str(areaCode) + "-" + str(middle3) + "-" + str(last4)
webbrowser.open(thatsThem)

syncMe = "https://sync.me/search/?number=1" + phoneNumber
webbrowser.open(syncMe)

whoCallsMe = "https://whocallsme.com/Phone-Number.aspx/" + phoneNumber
webbrowser.open(whoCallsMe)

zabaSearch = "https://www.zabasearch.com/phone/" + phoneNumber
webbrowser.open(zabaSearch)

peopleFinders = "https://www.peoplefinders.com/reverse-phone/searchresults?showAnimatedLoadingBar=true&search=Phone&phone=" + phoneNumber
webbrowser.open(peopleFinders)

okCaller = "https://www.okcaller.com/detail.php?number=" + phoneNumber
webbrowser.open(okCaller)

searchBug = "https://www.searchbug.com/tools/reverse-phone-lookup.aspx?TYPE=phonerev&TAG=tools&FULLPHONE=" + phoneNumber
webbrowser.open(searchBug)

yellowPages = "https://people.yellowpages.com/whitepages/phone-lookup?phone=" + phoneNumber
webbrowser.open(yellowPages)