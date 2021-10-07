# Generated by Django 3.1.12 on 2021-09-29 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0023_add_filebugzillacomponent'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugzillaSecurityGroup',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('product', models.CharField(db_index=True, max_length=60, unique=True)),
                ('security_group', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name_plural': 'bugzilla_security_groups',
                'db_table': 'bugzilla_security_group',
            },
        ),
    ]
