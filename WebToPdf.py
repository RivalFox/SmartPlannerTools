import pdfkit

path = r'.\wkhtmltopdf\bin\wkhtmltopdf.exe'

config = pdfkit.configuration(wkhtmltopdf = path)

pdfkit.from_url('https://catalog.columbusstate.edu/course-descriptions/cpsc/', r'.\Input\cpsc.pdf', configuration = config)
pdfkit.from_url('https://catalog.columbusstate.edu/course-descriptions/cybr/', r'.\Input\cybr.pdf', configuration = config)
