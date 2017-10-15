from ..models import Employer, ParttimeEmployer, FulltimeEmployer, Department, ParttimeSalary, FulltimeSalary
from ..serializers import PartTimeEmployerSerializer, FullTimeEmployerSerializer, BaseEmployerSerializer, \
    EmployerFilterSerializer, MaxPartTimeEmployerSalarySerializer, MaxFullTimeEmployerSalarySerializer, \
    EmployerListSalaryFilterSerializer
from ..constant import ErrorDefine
from ..infrastructures import ApiCustomException


class EmployerServices:
    def __init__(self):
        pass

    def get_all(self):
        employers = Employer.objects.all()

        for employer in employers:
            part_time_employer = ParttimeEmployer.objects.filter(employer_id=employer)
            full_time_employer = FulltimeEmployer.objects.filter(employer_id=employer)

            if part_time_employer.exists():
                employer.month_salary = None
                employer.salary_level = None
                employer.allowance = None

                employer.day_salary = part_time_employer.first().day_salary

            if full_time_employer.exists():
                employer.month_salary = full_time_employer.first().month_salary
                employer.salary_level = full_time_employer.first().salary_level
                employer.allowance = full_time_employer.first().allowance

                employer.day_salary = None

        serializer = EmployerFilterSerializer(employers, many=True)

        return serializer.data

    def create_part_time_employer(self, name, phone, birthday, day_salary, department_id):
        try:
            department = Department.objects.get(id=department_id)

            # create new Employer
            employer = Employer(name=name, phone=phone, birthday=birthday,
                                department_id=department)
            employer.save()

            # create new PartTimeEmployer
            part_time_employer = ParttimeEmployer(day_salary=day_salary, employer_id=employer)
            part_time_employer.save()

            employer.day_salary = day_salary

            serializer = PartTimeEmployerSerializer(employer)
            return serializer.data
        except Department.DoesNotExist:
            raise ApiCustomException(ErrorDefine.DEPARTMENT_NOT_FOUND)

    def create_full_time_employer(self, name, phone, birthday, department_id, month_salary, salary_level,
                                  allowance):
        try:
            department = Department.objects.get(id=department_id)

            # create new Employer
            employer = Employer(name=name, phone=phone, birthday=birthday,
                                department_id=department)
            employer.save()

            # create new PartTimeEmployer
            part_time_employer = FulltimeEmployer(month_salary=month_salary, employer_id=employer,
                                                  salary_level=salary_level, allowance=allowance)
            part_time_employer.save()

            employer.month_salary = month_salary
            employer.salary_level = salary_level
            employer.allowance = allowance

            serializer = FullTimeEmployerSerializer(employer)
            return serializer.data
        except Department.DoesNotExist:
            raise ApiCustomException(ErrorDefine.DEPARTMENT_NOT_FOUND)

    def get_by_department(self, department_id):
        employers = Employer.objects.filter(department_id_id=department_id)

        for employer in employers:
            part_time_employer = ParttimeEmployer.objects.filter(employer_id=employer)
            full_time_employer = FulltimeEmployer.objects.filter(employer_id=employer)

            if part_time_employer.exists():
                employer.month_salary = None
                employer.salary_level = None
                employer.allowance = None

                employer.day_salary = part_time_employer.first().day_salary

            if full_time_employer.exists():
                employer.month_salary = full_time_employer.first().month_salary
                employer.salary_level = full_time_employer.first().salary_level
                employer.allowance = full_time_employer.first().allowance

                employer.day_salary = None

        serializer = EmployerFilterSerializer(employers, many=True)

        return serializer.data

    def update_part_time_employer(self, employer_id, name, phone, birthday, day_salary, department_id):
        try:
            parttime_employer = ParttimeEmployer.objects.get(employer_id__id=employer_id)
            department = Department.objects.get(id=department_id)

            parttime_employer.day_salary = day_salary
            parttime_employer.save()

            employer = parttime_employer.employer_id
            employer.name = name
            employer.phone = phone
            employer.birthday = birthday
            employer.department_id = department
            employer.save()

            employer.day_salary = day_salary
            serializer = PartTimeEmployerSerializer(employer)

            return serializer.data
        except ParttimeEmployer.DoesNotExist:
            raise ApiCustomException(ErrorDefine.EMPLOYER_NOT_FOUND)
        except Department.DoesNotExist:
            raise ApiCustomException(ErrorDefine.DEPARTMENT_NOT_FOUND)

    def update_full_time_employer(self, employer_id, name, phone, birthday, department_id, month_salary, salary_level,
                                  allowance):
        try:
            fulltime_employer = FulltimeEmployer.objects.get(employer_id__id=employer_id)
            department = Department.objects.get(id=department_id)

            fulltime_employer.month_salary = month_salary
            fulltime_employer.salary_level = salary_level
            fulltime_employer.allowance = allowance

            fulltime_employer.save()

            employer = fulltime_employer.employer_id
            employer.name = name
            employer.phone = phone
            employer.birthday = birthday
            employer.department_id = department
            employer.save()

            employer.month_salary = month_salary
            employer.salary_level = salary_level
            employer.allowance = allowance

            serializer = FullTimeEmployerSerializer(employer)

            return serializer.data
        except FulltimeEmployer.DoesNotExist:
            raise ApiCustomException(ErrorDefine.EMPLOYER_NOT_FOUND)
        except Department.DoesNotExist:
            raise ApiCustomException(ErrorDefine.DEPARTMENT_NOT_FOUND)

    def get_max_month_salary(self, working_month_id):
        part_time_salary = ParttimeSalary.objects.filter(working_month_id=working_month_id)

        full_time_salary = FulltimeSalary.objects.filter(working_month_id=working_month_id)

        if part_time_salary.exists() and full_time_salary.exists():

            part_time_salary = part_time_salary.order_by('-total_salary').first()
            full_time_salary = full_time_salary.order_by('-total_salary').first()

            if part_time_salary.total_salary > full_time_salary.total_salary:
                employer = part_time_salary.part_time_employer_id.employer_id

                employer.month_salary = None
                employer.salary_level = None
                employer.allowance = None

                employer.day_salary = part_time_salary.part_time_employer_id.day_salary

                employer.total_salary = part_time_salary.total_salary
                employer.working_day_number = part_time_salary.working_day_number

                serializer = EmployerListSalaryFilterSerializer(employer)

                return serializer.data

            employer = full_time_salary.full_time_employer_id.employer_id

            employer.month_salary = full_time_salary.full_time_employer_id.month_salary
            employer.salary_level = full_time_salary.full_time_employer_id.salary_level
            employer.allowance = full_time_salary.full_time_employer_id.allowance

            employer.day_salary = None

            employer.total_salary = full_time_salary.total_salary
            employer.working_day_number = None

            serializer = EmployerListSalaryFilterSerializer(employer)

            return serializer.data

        if part_time_salary.exists():
            part_time_salary = part_time_salary.order_by('-total_salary').first()

            employer = part_time_salary.part_time_employer_id.employer_id

            employer.month_salary = None
            employer.salary_level = None
            employer.allowance = None

            employer.day_salary = part_time_salary.part_time_employer_id.day_salary

            employer.total_salary = part_time_salary.total_salary
            employer.working_day_number = part_time_salary.working_day_number

            serializer = EmployerListSalaryFilterSerializer(employer)

            return serializer.data

        if full_time_salary.exists():
            full_time_salary = full_time_salary.order_by('-total_salary').first()

            employer = full_time_salary.full_time_employer_id.employer_id

            employer.month_salary = full_time_salary.full_time_employer_id.month_salary
            employer.salary_level = full_time_salary.full_time_employer_id.salary_level
            employer.allowance = full_time_salary.full_time_employer_id.allowance

            employer.day_salary = None

            employer.total_salary = full_time_salary.total_salary
            employer.working_day_number = None

            serializer = EmployerListSalaryFilterSerializer(employer)

            return serializer.data

        return []

    # employer_type 1 is full-time, 2 part-time
    def get_list_salary_by_type(self, employer_type, working_month_id):
        if employer_type != 1 and employer_type != 2:
            raise ApiCustomException(ErrorDefine.EMPLOYER_TYPE_ERROR)

        exclude_queryset = {}

        if employer_type == 1:
            exclude_queryset = ParttimeEmployer.objects.all().values('employer_id_id')

        if employer_type == 2:
            exclude_queryset = FulltimeEmployer.objects.all().values('employer_id_id')

        employers = Employer.objects.all().exclude(id__in=exclude_queryset)

        print employers

        for employer in employers:
            part_time_employer = ParttimeEmployer.objects.filter(employer_id=employer)
            full_time_employer = FulltimeEmployer.objects.filter(employer_id=employer)

            if part_time_employer.exists():
                employer.month_salary = None
                employer.salary_level = None
                employer.allowance = None

                employer.day_salary = part_time_employer.first().day_salary

                employer.total_salary = None
                employer.working_day_number = None

                part_time_salary = ParttimeSalary.objects.filter(part_time_employer_id=part_time_employer,
                                                                 working_month_id_id=working_month_id)
                if part_time_salary.exists():
                    employer.total_salary = part_time_salary.first().total_salary
                    employer.working_day_number = part_time_salary.first().working_day_number

            if full_time_employer.exists():
                employer.month_salary = full_time_employer.first().month_salary
                employer.salary_level = full_time_employer.first().salary_level
                employer.allowance = full_time_employer.first().allowance

                employer.day_salary = None

                employer.total_salary = None
                employer.working_day_number = None

                full_time_salary = FulltimeSalary.objects.filter(full_time_employer_id=full_time_employer,
                                                                 working_month_id_id=working_month_id)

                if full_time_salary.exists():
                    employer.total_salary = full_time_salary.first().total_salary

        if employers.exists():
            serializer = EmployerListSalaryFilterSerializer(employers, many=True)

            return serializer.data
        return []
