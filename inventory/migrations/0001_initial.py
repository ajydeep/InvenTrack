
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='product name', max_length=100, unique=True)),
                ('description', models.TextField(blank=True, help_text='product description', null=True)),
                ('price', models.DecimalField(decimal_places=2, help_text='price of product', max_digits=10)),
                ('quantity', models.IntegerField(default=0, help_text='quantity in stock currently')),
                ('low_stock_threshold', models.IntegerField(db_default=10, help_text='for low stock alert')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
