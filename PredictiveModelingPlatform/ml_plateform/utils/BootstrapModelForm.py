from django import forms

# 套用bootstrap樣式的modelform，用來被其他modelform繼承
class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #在表單初始化時，我們為每個表單欄位自動添加 CSS 類別 form-control，
        #這樣表單的輸入欄位就會使用 Bootstrap 的樣式。
        #name就是欄位名稱
        #循環modelform中所有欄位，然後給每個欄位設置插件
        for name, field in self.fields.items():
            #欄位中若有屬性，要順便保留原來的屬性，如果沒有屬性的話才直接設置
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class" : "form-control",
                    "placeholder":field.label
                
                }


class BootstrapForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #在表單初始化時，我們為每個表單欄位自動添加 CSS 類別 form-control，
        #這樣表單的輸入欄位就會使用 Bootstrap 的樣式。
        #name就是欄位名稱
        #循環modelform中所有欄位，然後給每個欄位設置插件
        for name, field in self.fields.items(): 
            #欄位中若有屬性，要順便保留原來的屬性，如果沒有屬性的話才直接設置
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class" : "form-control",
                    "placeholder":field.label
                
                }
