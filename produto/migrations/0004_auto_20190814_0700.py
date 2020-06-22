

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_variacao_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variacao',
            name='nome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
