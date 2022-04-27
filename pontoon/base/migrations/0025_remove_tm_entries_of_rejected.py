# Generated by Django 3.2.10 on 2022-04-22 12:12

from django.db import migrations


def remove_tm_entries_of_rejected(apps, schema_editor):
    TranslationMemoryEntry = apps.get_model("base", "TranslationMemoryEntry")
    TranslationMemoryEntry.objects.filter(translation__rejected=True).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0024_fuzzy_to_pretranslated_strings"),
    ]

    operations = [
        migrations.RunPython(
            code=remove_tm_entries_of_rejected,
            reverse_code=migrations.RunPython.noop,
        ),
    ]