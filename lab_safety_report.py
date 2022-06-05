from docxtpl import DocxTemplate, InlineImage
import jinja2
from docx.shared import Mm
import calendar


class lab_safety_report():
    def __init__(self, template_docx, 
            company='너네회사', 
            name='우주정거장', 
            buildingNo='999', 
            roomNo='999', 
            safety_manager='너', 
            boss='너네보스'):

        self.num_rows = 29
        self.num_cols = 31
        self.doc = DocxTemplate(template_docx)

        self.company = company
        self.name = name
        self.buildingNo = buildingNo
        self.roomNo = roomNo
        self.safety_manager = safety_manager
        self.boss =boss
                
    
    def generate(self, output_docx, year, month, day=31):
        
        self.doc.render(self.fill_report(year, month, day))
        self.doc.save(output_docx)

    def fill_report(self, year, month, day=31):
        payload = {
            'date': {
                'year': year,
                'mon' : month
            },
            'lab': {
                'company': self.company,
                'name': self.name,
                'buildingNo': self.buildingNo,
                'roomNo' : self.roomNo,
                'safety_manager' : self.safety_manager,
                'boss' : self.boss
            },
            'myimage' : InlineImage(self.doc,'./resources/circle1.png',width=Mm(3)),
            'myimage2' : InlineImage(self.doc,'./resources/circle2.png',width=Mm(3)),
            'myimage3' : InlineImage(self.doc,'./resources/circle3.png',width=Mm(3)),
            'content': {
                'rows': []
            }
        }
        payload['content']['rows'] = self.genCals(year, month, day)
        return payload


    def genCals(self, year, month, day=31):
        cals = []
        for r in range(1, self.num_rows + 1):
            cal = []
            for i in range(1, self.num_cols + 1):    
                if i <= day: 
                    try:
                        weekday = calendar.weekday(year, month, i)
                        if(r > 13 and r < self.num_rows -1 ): cal.append('-')
                        else:
                            if(weekday == 5 or weekday == 6): cal.append('-')
                            elif(weekday >= 0 and weekday < 5): cal.append('o')
                    except:        
                        cal.append('-')
                else:
                    cal.append(' ')

            cals.append(cal)
        return cals

# if __name__ == '__main__':
#     generator = lab_safety_report('./template/lab_safety_report_template.docx')
#     generator.generate('./output/lab_safety_report.docx', 2021,4,10)




