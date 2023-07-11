import random
from django.shortcuts import get_object_or_404, render, redirect
from .forms import SubjectStudentForm
from .models import Distribution

# def distribute(items, groups):
#     random.shuffle(items)
#     num_items = len(items)
#     num_groups = len(groups)
#     group_size = num_items // num_groups
#     remaining_items = num_items % num_groups

#     result = {}
#     start_index = 0
#     for i, group in enumerate(groups):
#         group_size_with_extra_item = group_size + 1 if i < remaining_items else group_size
#         end_index = start_index + group_size_with_extra_item
#         result[group] = items[start_index:end_index]
#         start_index = end_index

#     remaining_items_list = items[-remaining_items:]
#     for group in result:
#         result[group].extend(remaining_items_list)
#    return result

def distribute(items, groups):
    random.shuffle(items)
    num_items = len(items)
    num_groups = len(groups)

    result = {}
    for i, group in enumerate(groups):
        group_size = num_items // num_groups
        if i < num_items % num_groups:
            group_size += 1
        result[group] = items[i * group_size: (i + 1) * group_size]

    return result

def subject_student_view(request):
    if request.method == 'POST':
        form = SubjectStudentForm(request.POST)
        if form.is_valid():
            students = form.cleaned_data['students'].split(',')
            subjects = form.cleaned_data['subjects'].split(',')

            result = {}
            if len(students) >= len(subjects):
                result = distribute(students, subjects)
            else:
                result = distribute(subjects, students)

            distribution = Distribution(students=form.cleaned_data['students'], subjects=form.cleaned_data['subjects'], result=result)
            distribution.save()

            return render(request, 'result.html', {'result': result, 'students': form.cleaned_data['students'], 'subjects': form.cleaned_data['subjects'], 'distribution_id': distribution.id})

    else:
        form = SubjectStudentForm()

    return render(request, 'subject_student.html', {'form': form})

def edit_result(request, distribution_id):
    distribution = get_object_or_404(Distribution, id=distribution_id)

    if request.method == 'POST':
        form = SubjectStudentForm(request.POST)
        if form.is_valid():
            students = form.cleaned_data['students'].split(',')
            subjects = form.cleaned_data['subjects'].split(',')

            result = {}
            if len(students) >= len(subjects):
                result = distribute(students, subjects)
            else:
                result = distribute(subjects, students)

            distribution.students = form.cleaned_data['students']
            distribution.subjects = form.cleaned_data['subjects']
            distribution.result = result
            distribution.save()

            return render(request, 'result.html', {'result': result, 'students': form.cleaned_data['students'], 'subjects': form.cleaned_data['subjects'], 'distribution_id': distribution.id})

    else:
        initial_data = {
            'students': distribution.students,
            'subjects': distribution.subjects
        }
        form = SubjectStudentForm(initial=initial_data)

    distribution.save()

    return render(request, 'edit_result.html', {'form': form, 'distribution_id': distribution_id})


# def delete_result(request, distribution_id):
#     distribution = get_object_or_404(Distribution, id=distribution_id)
#     distribution.delete()
#     return redirect('subject-student')

def delete_result(request, distribution_id):
    distribution = get_object_or_404(Distribution, id=distribution_id)

    if request.method == 'POST':
        delete_list = request.POST.get('delete_list')

        result = {}
        if delete_list == 'students':
            students = distribution.students.split(',')
            distribution.students = ''
            result['students'] = students
        elif delete_list == 'subjects':
            subjects = distribution.subjects.split(',')
            distribution.subjects = ''
            result['subjects'] = subjects

        distribution.save()

        return render(request, 'delete_result.html', {'result': result})

    return render(request, 'delete_confirmation.html', {'distribution': distribution, 'result': None})


