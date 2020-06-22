

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_variacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='variacao',
            name='nome',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
