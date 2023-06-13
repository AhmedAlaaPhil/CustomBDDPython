BDD = {

    "Given": {
        "BaseURL": "HTTPS:/BaseURL",
        "Headers": {"Auth": "Basic"},
        "PathParams": {"Param1": "/Param"},
        "QueryParams": {"Q1": "123", "Q2": "ABC"}
    },

    "When": {
        "HTTPMethod": "GET"

    },
    "Then": {
        "Assert": {
            "Code": 200
        }
    }

}

StrURL = ""

for str, info in BDD.items():
    if str == "Given":
        print(str)
        for element, data in info.items():
            if element == "BaseURL":
                StrURL = StrURL + element
            if element == "PathParams":
                for path in data:
                    StrURL = StrURL + data[path]
            if element == "QueryParams":
                StrURL = StrURL + "?"
                for path in data:
                    q = path+"="+data[path]+"&"
                    StrURL = StrURL + q

print(StrURL)
