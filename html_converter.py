from html2image import Html2Image

hti = Html2Image()
file_path = '/Users/joeg/Project/Logo/logo-design-html/design/zero_nine_pandan.html'
out_name = 'pandan_logo.png'
hti.screenshot(html_file=file_path, save_as=out_name)