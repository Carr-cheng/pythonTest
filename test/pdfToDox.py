from pdf2docx import parse

def pdf2doc():
    pdf_file = 'D:\学习资料/In-Flight_Energy-Driven_Composition_of_Drone_Swarm_Services(1).pdf'
    docx_file = 'D:\学习资料/sample.docx'
    parse(pdf_file,docx_file)