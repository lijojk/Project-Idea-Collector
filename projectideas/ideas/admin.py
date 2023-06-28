from django.contrib import admin
from .models import Course, ProjectIdeas, Technology

# modules for pdf section
from django.http import HttpResponse
from reportlab.pdfgen import canvas


# for passing cr_user to ExportProjectIdeas
class ParentModelSuper(admin.ModelAdmin):
    list_display = ('cr_user',)


# function for pdf export
def make_pdf(cur_class, req, queryset):
    # Create a response object with PDF content type
    response = HttpResponse(content_type='application/pdf')
    # Set the filename of the generated PDF
    response['Content-Disposition'] = 'attachment; filename="Project Details.pdf"'

    # Create a PDF canvas
    pdf = canvas.Canvas(response)
    # Fetch model values and write them to the PDF
    for obj in queryset:
        p_project_title = obj.project_Title
        c_created_user = obj.cr_user
        c_course = obj.course
        p_project_type = obj.project_Type
        t_technology = obj.technology
        d_description = obj.description

        # Write the attribute values to the PDF
        pdf.drawString(200, 800, f"PROJECT DETAILS")
        pdf.drawString(100, 770, f"Project Title:       {p_project_title}")
        pdf.drawString(100, 750, f"Created User:     {c_created_user}")
        pdf.drawString(100, 730, f"Course:               {c_course}")
        pdf.drawString(100, 710, f"Project Type:       {p_project_type}")
        pdf.drawString(100, 690, f"Technology:        {t_technology}")
        pdf.drawString(100, 670, f"Description:         {d_description}")

        # Move to the next page if needed
        pdf.showPage()
    # Close the PDF canvas
    pdf.save()

    return response


make_pdf.short_description = "Export to pdf"


class ExportProjectIdeas(ParentModelSuper):
    list_display = ParentModelSuper.list_display + (
        'course', 'project_Type', 'description', 'technology', 'project_Title')
    actions = [make_pdf]


# Registering models on admin site
admin.site.register(Course)
admin.site.register(ProjectIdeas, ExportProjectIdeas)
admin.site.register(Technology)
