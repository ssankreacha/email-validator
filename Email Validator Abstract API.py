import requests

# Replace with your Abstract API Key
# Login via Abstract API, find your API key. There are a total of 100 requests on the free plan as of 2025.
API_KEY = " "


def validate_email_api(email):
    """
    Uses Abstract API to validate an email address.
    """
    url = f"https://emailvalidation.abstractapi.com/v1/?api_key={API_KEY}&email={email}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print("❌ API Error: Unable to fetch data.")
            return

        # Extract key validation details
        is_valid = data.get("is_valid_format", {}).get("value", False)
        is_deliverable = data.get("deliverability", "") == "DELIVERABLE"
        is_disposable = data.get("is_disposable_email", {}).get("value", False)

        if not is_valid:
            print("❌ Invalid email format.")
            return

        if not is_deliverable:
            print("❌ This email is not deliverable (it may not exist).")
            return

        if is_disposable:
            print("⚠️ Warning: This is a disposable email address.")

        print("✅ The email is valid and deliverable!")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    user_email = input("Enter an email address to validate: ").strip()
    validate_email_api(user_email)

