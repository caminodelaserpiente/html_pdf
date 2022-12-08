import jinja2
import pdfkit
from datetime import datetime


def main():
    factura_to = input("factura to: >>> ")
    address = input("address: >>>")
    date = datetime.today().strftime("%d %b %Y")

    context = {'factura_to': factura_to, 
                'address': address, 
                'date': date}

    # generate html template
    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    html_path = 'fac_example.html' # name file html
    template = template_env.get_template(html_path)
    html_template = template.render(context) # render dictionary in pdf

    # generated pdf
    config = pdfkit.configuration(wkhtmltopdf='/home/gnu/anaconda3/envs/python/bin/wkhtmltopdf')
    output_pdf = 'pdf_generated.pdf'
    pdfkit.from_string(html_template, output_pdf, configuration=config)


if __name__ == "__main__":
    main()