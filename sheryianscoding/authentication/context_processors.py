from .models import Students

def student_context(request):
    student_id = request.session.get('student_id')
    student = None
    if student_id:
        student = Students.objects.filter(id=student_id).first()
    return {
        'logged_in_student': student
    }