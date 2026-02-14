# Pydantic Learning Guide | পাইডান্টিক শেখার গাইড

A comprehensive guide to learning Pydantic through practical examples. This repository contains 6 progressive parts covering essential Pydantic features from basic validation to advanced model handling.

একটি সম্পূর্ণ গাইড যেখানে ব্যবহারিক উদাহরণের মাধ্যমে Pydantic শেখা যাবে। এই রিপোজিটরিতে ৬টি ধাপে Pydantic এর মূল বিষয়গুলো কভার করা হয়েছে - বেসিক ভ্যালিডেশন থেকে শুরু করে অ্যাডভান্সড মডেল হ্যান্ডলিং পর্যন্ত।

## Overview | সংক্ষিপ্ত বিবরণ

Pydantic is a data validation library for Python that uses type annotations to validate data and provide helpful error messages. This guide demonstrates key Pydantic concepts through a patient management system example.

Pydantic হলো Python এর একটি ডাটা ভ্যালিডেশন লাইব্রেরি যা টাইপ অ্যানোটেশন ব্যবহার করে ডাটা যাচাই করে এবং সহায়ক এরর মেসেজ দেয়। এই গাইডে একটি রোগী ম্যানেজমেন্ট সিস্টেমের উদাহরণের মাধ্যমে Pydantic এর মূল ধারণাগুলো দেখানো হয়েছে।

## Table of Contents | সূচিপত্র

- [Part 1: Field Validation and Constraints | পার্ট ১: ফিল্ড ভ্যালিডেশন এবং কন্সট্রেইন্টস](#part-1-field-validation-and-constraints)
- [Part 2: Custom Field Validators | পার্ট ২: কাস্টম ফিল্ড ভ্যালিডেটর](#part-2-custom-field-validators)
- [Part 3: Model Validators | পার্ট ৩: মডেল ভ্যালিডেটর](#part-3-model-validators)
- [Part 4: Computed Fields | পার্ট ৪: কম্পিউটেড ফিল্ড](#part-4-computed-fields)
- [Part 5: Nested Models | পার্ট ৫: নেস্টেড মডেল](#part-5-nested-models)
- [Part 6: Model Serialization | পার্ট ৬: মডেল সিরিয়ালাইজেশন](#part-6-model-serialization)

## Prerequisites

```bash
pip install pydantic[email]
```

## Part 1: Field Validation and Constraints | পার্ট ১: ফিল্ড ভ্যালিডেশন এবং কন্সট্রেইন্টস

Learn how to use Pydantic's built-in field validators and constraints.

Pydantic এর বিল্ট-ইন ফিল্ড ভ্যালিডেটর এবং কন্সট্রেইন্ট কীভাবে ব্যবহার করতে হয় তা শিখুন।

**Key Concepts: | মূল ধারণা:**
- `Field()` for adding constraints and metadata | কন্সট্রেইন্ট এবং মেটাডাটা যোগ করার জন্য
- `EmailStr` for email validation | ইমেইল যাচাই করার জন্য
- `AnyUrl` for URL validation | URL যাচাই করার জন্য
- `Annotated` for type hints with metadata | মেটাডাটা সহ টাইপ হিন্ট এর জন্য
- Numeric constraints (`gt`, `lt`) | সংখ্যার সীমা নির্ধারণ (বড়, ছোট)
- `Optional` fields | ঐচ্ছিক ফিল্ড
- `strict` mode to prevent type coercion | টাইপ কনভার্সন বন্ধ করার জন্য স্ট্রিক্ট মোড

**Example:**
```python
class patient(BaseModel):
    name: Annotated[str, Field(max_length=50)]
    email: EmailStr
    linkedIn_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    allergies: Optional[List[str]] = Field(max_length=5)
```

## Part 2: Custom Field Validators | পার্ট ২: কাস্টম ফিল্ড ভ্যালিডেটর

Implement custom validation logic for individual fields.

প্রতিটি ফিল্ডের জন্য নিজস্ব ভ্যালিডেশন লজিক তৈরি করুন।

**Key Concepts: | মূল ধারণা:**
- `@field_validator` decorator | ডেকোরেটর
- Custom validation functions | নিজস্ব ভ্যালিডেশন ফাংশন
- Value transformation | ভ্যালু পরিবর্তন
- Validation modes (`before` and `after`) | ভ্যালিডেশন মোড (আগে এবং পরে)
- Type coercion handling | টাইপ কনভার্সন হ্যান্ডলিং

**Example:**
```python
@field_validator('email')
@classmethod
def email_validator(cls, value):
    valid_domain = ['seu.com', 'ewu.com', 'nsu.com']
    domain_name = value.split('@')[-1]
    if domain_name not in valid_domain:
        raise ValueError('Not in valid Domain')
    return value

@field_validator('name')
@classmethod
def transform_name(cls, value):
    return value.upper()
```

## Part 3: Model Validators | পার্ট ৩: মডেল ভ্যালিডেটর

Validate relationships between multiple fields using model validators.

একাধিক ফিল্ডের মধ্যে সম্পর্ক যাচাই করুন মডেল ভ্যালিডেটর ব্যবহার করে।

**Key Concepts: | মূল ধারণা:**
- `@model_validator` decorator | ডেকোরেটর
- Cross-field validation | একাধিক ফিল্ড একসাথে যাচাই করা
- Business logic enforcement | বিজনেস লজিক প্রয়োগ করা
- Access to entire model instance | সম্পূর্ণ মডেল ইনস্ট্যান্স এক্সেস করা

**Example: | উদাহরণ:**
```python
@model_validator(mode='after')
def transfer_age(cls, model):
    if model.age > 60 and 'emergency' not in model.contact_details:
        raise ValueError('patient older then 60 so it must be an emergency contact')
    return model
```

**Explanation | ব্যাখ্যা:** যদি রোগীর বয়স ৬০ এর বেশি হয় তাহলে তার ইমার্জেন্সি কন্টাক্ট থাকতে হবে। এটা একটা বিজনেস রুল যা মডেল ভ্যালিডেটর দিয়ে চেক করা হচ্ছে।

## Part 4: Computed Fields | পার্ট ৪: কম্পিউটেড ফিল্ড

Create derived fields that are automatically calculated from other fields.

এমন ফিল্ড তৈরি করুন যা অন্য ফিল্ড থেকে অটোমেটিক ভাবে ক্যালকুলেট হয়।

**Key Concepts: | মূল ধারণা:**
- `@computed_field` decorator | ডেকোরেটর
- `@property` decorator | প্রপার্টি ডেকোরেটর
- Automatic calculation | অটোমেটিক ক্যালকুলেশন
- Read-only fields | শুধুমাত্র পড়া যায় এমন ফিল্ড

**Example: | উদাহরণ:**
```python
@computed_field
@property
def BMI(self) -> float:
    bmi = round((self.weight / self.height**2), 2)
    return bmi
```

**Usage: | ব্যবহার:**
```python
patient_info = {
    "name": "abdullah al masum",
    "weight": 55.6,
    "height": 1.7,
    # ... other fields
}
patient1 = patient(**patient_info)
print(patient1.BMI)  # Automatically calculated | অটোমেটিক ক্যালকুলেট হবে
```

**Explanation | ব্যাখ্যা:** BMI ফিল্ডটি আমাদের সেট করতে হয় না, এটি ওজন এবং উচ্চতা থেকে অটোমেটিক ক্যালকুলেট হয়ে যায়।

## Part 5: Nested Models | পার্ট ৫: নেস্টেড মডেল

Build complex data structures using nested Pydantic models.

নেস্টেড Pydantic মডেল ব্যবহার করে জটিল ডাটা স্ট্রাকচার তৈরি করুন।

**Key Concepts: | মূল ধারণা:**
- Model composition | মডেল কম্পোজিশন
- Nested validation | নেস্টেড ভ্যালিডেশন
- Hierarchical data structures | স্তরবিন্যাস ডাটা স্ট্রাকচার
- Accessing nested fields | নেস্টেড ফিল্ড এক্সেস করা

**Example: | উদাহরণ:**
```python
class Address(BaseModel):
    road_no: int
    house_no: int
    city: str
    pin: int

class patient(BaseModel):
    name: str
    age: int
    address: Address

# Usage | ব্যবহার
address1 = Address(**Address_info)
patient1 = patient(name="abdullah", age=22, address=address1)
print(patient1.address.city)  # Access nested field | নেস্টেড ফিল্ড এক্সেস
```

**Explanation | ব্যাখ্যা:** এখানে Address একটা আলাদা মডেল যেটা patient মডেলের ভিতরে ব্যবহার হচ্ছে। এভাবে জটিল ডাটা স্ট্রাকচার সহজে তৈরি করা যায়।

## Part 6: Model Serialization | পার্ট ৬: মডেল সিরিয়ালাইজেশন

Control how models are serialized to dictionaries and JSON.

মডেল কীভাবে ডিকশনারি এবং JSON এ কনভার্ট হবে তা কন্ট্রোল করুন।

**Key Concepts: | মূল ধারণা:**
- `model_dump()` - Convert to dictionary | ডিকশনারিতে কনভার্ট
- `model_dump_json()` - Convert to JSON string | JSON স্ট্রিং এ কনভার্ট
- `exclude_unset=True` - Exclude fields not explicitly set | যে ফিল্ড সেট করা হয়নি তা বাদ দেওয়া
- Default values handling | ডিফল্ট ভ্যালু হ্যান্ডলিং

**Example: | উদাহরণ:**
```python
class patient(BaseModel):
    name: str = "abdullah"  # Default value | ডিফল্ট ভ্যালু
    age: int
    address: Address

patient1 = patient(age=22, address=address1)
# Only includes fields that were explicitly set
# শুধুমাত্র যে ফিল্ডগুলো সেট করা হয়েছে সেগুলো রাখবে
json_output = patient1.model_dump_json(exclude_unset=True)
```

**Explanation | ব্যাখ্যা:** `exclude_unset=True` ব্যবহার করলে শুধু যে ফিল্ডগুলো আমরা সেট করেছি (যেমন age, address) সেগুলো আসবে। name ফিল্ডটি যেহেতু ডিফল্ট ভ্যালু ব্যবহার করছে এবং আমরা সেট করিনি, তাই সেটা আসবে না।

## Common Patterns | সাধারণ প্যাটার্ন

### Creating Model Instances | মডেল ইনস্ট্যান্স তৈরি করা
```python
# From dictionary | ডিকশনারি থেকে
patient_data = {"name": "John", "age": 30, ...}
patient = patient(**patient_data)

# Direct instantiation | সরাসরি তৈরি করা
patient = patient(name="John", age=30, ...)
```

### Accessing Model Data | মডেল ডাটা এক্সেস করা
```python
# Access fields directly | সরাসরি ফিল্ড এক্সেস
print(patient.name)
print(patient.email)

# Convert to dictionary | ডিকশনারিতে কনভার্ট
patient_dict = patient.model_dump()

# Convert to JSON | JSON এ কনভার্ট
patient_json = patient.model_dump_json()
```

### Validation Flow | ভ্যালিডেশন ফ্লো
1. Type coercion (if not strict mode) | টাইপ কনভার্সন (যদি স্ট্রিক্ট মোড না থাকে)
2. Field validators (in order of definition) | ফিল্ড ভ্যালিডেটর (যে ক্রমে লেখা আছে)
3. Model validators | মডেল ভ্যালিডেটর
4. Computed fields calculation | কম্পিউটেড ফিল্ড ক্যালকুলেশন

## Benefits of Using Pydantic | Pydantic ব্যবহারের সুবিধা

- **Type Safety | টাইপ সেফটি**: Catch errors at validation time, not runtime | রানটাইমে নয়, ভ্যালিডেশনের সময়ই এরর ধরা পড়ে
- **Auto Documentation | অটো ডকুমেন্টেশন**: Self-documenting code through type hints | টাইপ হিন্ট দিয়ে কোড নিজেই ডকুমেন্ট হয়ে যায়
- **IDE Support | IDE সাপোর্ট**: Better autocomplete and type checking | ভালো অটোকমপ্লিট এবং টাইপ চেকিং
- **Data Parsing | ডাটা পার্সিং**: Automatic conversion from JSON, dict, etc. | JSON, dict থেকে অটোমেটিক কনভার্সন
- **Validation | ভ্যালিডেশন**: Rich validation with helpful error messages | সহায়ক এরর মেসেজ সহ শক্তিশালী ভ্যালিডেশন
- **Performance | পারফরম্যান্স**: Fast validation using Rust-based core (Pydantic V2) | Rust দিয়ে তৈরি তাই দ্রুত ভ্যালিডেশন

## Error Handling | এরর হ্যান্ডলিং

Pydantic provides detailed validation errors:

Pydantic বিস্তারিত ভ্যালিডেশন এরর দেয়:

```python
try:
    patient1 = patient(**invalid_data)
except ValidationError as e:
    print(e.json())  # Detailed error information | বিস্তারিত এরর তথ্য
```

## Best Practices | সেরা অনুশীলন

1. Use `Annotated` for field metadata to keep type hints clean | টাইপ হিন্ট পরিষ্কার রাখতে `Annotated` ব্যবহার করুন
2. Leverage `Field()` for constraints and documentation | কন্সট্রেইন্ট এবং ডকুমেন্টেশনের জন্য `Field()` ব্যবহার করুন
3. Use custom validators for domain-specific logic | নিজস্ব লজিকের জন্য কাস্টম ভ্যালিডেটর ব্যবহার করুন
4. Keep validation logic in validators, not in application code | ভ্যালিডেশন লজিক ভ্যালিডেটরে রাখুন, অ্যাপ্লিকেশন কোডে নয়
5. Use nested models for complex data structures | জটিল ডাটা স্ট্রাকচারের জন্য নেস্টেড মডেল ব্যবহার করুন
6. Set appropriate default values | উপযুক্ত ডিফল্ট ভ্যালু সেট করুন
7. Use `strict=True` when type coercion is undesirable | টাইপ কনভার্সন চাইলে না `strict=True` ব্যবহার করুন

## Running the Examples | উদাহরণ রান করা

Each part is standalone and can be run independently:

প্রতিটি পার্ট আলাদাভাবে রান করা যাবে:

```bash
python part1.py
python part2.py
# ... and so on | ... এভাবে বাকিগুলো
```

## Contributing | অবদান

Feel free to add more examples or improvements to this learning guide!

এই লার্নিং গাইডে আরো উদাহরণ বা উন্নতি যোগ করতে পারেন!

## License

MIT License

---

**Happy Learning! 🚀**
