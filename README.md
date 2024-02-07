```command
behave -f behave_html_formatter:HTMLFormatter -o behave-report.html
behave --tags=invalidPassword   #rulam toate testele care au tag-ul respectiv
behave -f behave_html_formatter:HTMLFormatter -o behave-report.html --tags=invalidPassword #rulam doar testele cu tags si primim raport
behave -f html -o behave-report.html    #utilizabil doar daca este creat fisierul behave.ini care sa contina [behave.formatters]
                                                                                                             html = behave_html_formatter:HTMLFormatter
```