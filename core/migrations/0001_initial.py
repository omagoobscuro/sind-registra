# Generated by Django 2.2 on 2019-05-20 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('inicio', models.TimeField(unique=True)),
                ('fim', models.TimeField()),
                ('assunto', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('A', 'Atendido'), ('NA', 'Nao atendido'), ('NC', 'Nao compareceu')], default='A', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='DebitoTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name_plural': 'Debitos Totais',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=12)),
                ('cnpj', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LancamentoTotal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Empresa')),
            ],
            options={
                'verbose_name_plural': 'lançamentos Totais',
            },
        ),
        migrations.CreateModel(
            name='Lancamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('vencimento', models.DateField()),
                ('data_envio', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('P', 'Pago'), ('N', 'Não Pago')], max_length=1, verbose_name='Pago')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Empresa')),
            ],
            options={
                'verbose_name_plural': 'lançamentos',
            },
        ),
        migrations.CreateModel(
            name='Financeiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consulta', models.DateTimeField()),
                ('debito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DebitoTotal')),
                ('lancamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.LancamentoTotal')),
            ],
        ),
        migrations.AddField(
            model_name='debitototal',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Empresa'),
        ),
        migrations.CreateModel(
            name='Debito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('vencimento', models.DateField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Associado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=12)),
                ('data_nascimento', models.DateField()),
                ('data_filiacao', models.DateField()),
                ('cpf', models.CharField(max_length=12)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Empresa')),
            ],
        ),
    ]
