# 📧 Email Validator – Python Project

## 📌 Project Description
The **Email Validator** is a **Python-based CLI tool** that validates email addresses by checking:

✅ **Basic email format** (ensuring "@" and valid domain structure).  
✅ **Domain existence** (verifies whether the domain has real mail servers).  
✅ **Email typo detection** (suggests corrections for common domain typos).  

---

## 🛠️ Features
- **Regex Format Validation**: Ensures the email follows standard syntax.
- **Domain MX Record Check**: Verifies if the domain has valid mail servers.
- **Typo Detection & Auto-Correction**: Suggests domain corrections for misspelled domains (e.g., `"gamil.com" → "gmail.com"`).
- **CLI Interface**: Simple command-line interaction for users.

---

## 🏆 Future Enhancements
- **Add support for detecting temporary/disposable emails.**
- **Improve typo correction with Levenshtein Distance. **
- **Implement real-time email verification using APIs (alternative version available).**
