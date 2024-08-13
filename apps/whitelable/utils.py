from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Profile, Company, MobileNumber

@login_required
def get_user_data(request):
    user_data = {
        'SITE_NAME': 'Techpath Research and Development PVT',
        'GLOBAL_ANNOUNCEMENT': 'Welcome to our website!',
    }

    # Attempt to add Profile information to user_data
    try:
        profile = Profile.objects.get(user=request.user)
        user_data['PROFILE_NAME'] = profile.name
        user_data['PROFILE_EMAIL'] = profile.email

        # Including MobileNumbers directly in the user_data
        mobile_numbers = profile.mobile_numbers.all()
        user_data['MOBILE_NUMBERS'] = [number.number for number in mobile_numbers]
            
    except Profile.DoesNotExist:
        user_data['Profile_Info'] = "No profile found"

    # Attempt to add Company information to user_data
    try:
        company = Company.objects.get(user=request.user)
        user_data['COMPANY_NAME'] = company.name
        user_data['Company_Logo_URL'] = company.logo.url if company.logo else None
        user_data['COMPANY_REG_NO'] = company.reg_no
        user_data['COMPANY_STATE_CODE'] = company.state_code
        user_data['COMPANY_SERVICE_REGD'] = company.service_regd
        user_data['COMPANY_BANK_NAME'] = company.bank_name
        user_data['COMPANY_ACCOUNT_NUMBER'] = company.account_number
        user_data['COMPANY_IFSC'] = company.ifsc
        user_data['COMPANY_ADDRESS'] = company.address
        user_data['COMPANY_BILLING_STATEMENT'] = company.billing_statement
        
    except Company.DoesNotExist:
        user_data['Company_Info'] = "No company information found"

    return user_data
