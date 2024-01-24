from django import forms
from email_app.tasks import send_review_email_task


class ReviewForm(forms.Form):
    name = forms.CharField(
        label="Firstname",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Firstname",
                "id": "form-firstname",
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Email",
                "id": "form-email",
            }
        )
    )
    review = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "Review",
                "id": "form-review",
            }
        )
    )

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        send_review_email_task.delay(
            self.cleaned_data["name"],
            self.cleaned_data["email"],
            self.cleaned_data["review"],
        )
