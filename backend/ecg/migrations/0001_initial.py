# Generated by Django 4.2.11 on 2024-05-09 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baseline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_dt', models.DateTimeField(auto_now_add=True, db_column='INS_DT')),
                ('upt_dt', models.DateTimeField(auto_now=True, db_column='UPD_DT')),
                ('mean_hr', models.FloatField(blank=True, db_column='HRV_MEAN_HR', null=True)),
                ('mean_rr', models.FloatField(blank=True, db_column='HRV_MEAN_RR', null=True)),
                ('sdnn', models.FloatField(blank=True, db_column='HRV_SDNN', null=True)),
                ('rmssd', models.FloatField(blank=True, db_column='HRV_RMSSD', null=True)),
                ('pnn50', models.FloatField(blank=True, db_column='HRV_pNN50', null=True)),
                ('pnn20', models.FloatField(blank=True, db_column='HRV_pNN20', null=True)),
                ('pnn10', models.FloatField(blank=True, db_column='HRV_pNN10', null=True)),
                ('pnn05', models.FloatField(blank=True, db_column='HRV_pNN05', null=True)),
                ('vlf', models.FloatField(blank=True, db_column='HRV_VLF', null=True)),
                ('lf', models.FloatField(blank=True, db_column='HRV_LF', null=True)),
                ('hf', models.FloatField(blank=True, db_column='HRV_HF', null=True)),
                ('lf_hf_ratio', models.FloatField(blank=True, db_column='HRV_LF_HF_RATIO', null=True)),
                ('sd1', models.FloatField(blank=True, db_column='HRV_SD1', null=True)),
                ('sd2', models.FloatField(blank=True, db_column='HRV_SD2', null=True)),
                ('sd1_sd2_ratio', models.FloatField(blank=True, db_column='HRV_SD1_SD2_RATIO', null=True)),
            ],
            options={
                'db_table': 'OC_HRV_BASELINE',
            },
        ),
        migrations.CreateModel(
            name='Recovery1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_dt', models.DateTimeField(auto_now_add=True, db_column='INS_DT')),
                ('upt_dt', models.DateTimeField(auto_now=True, db_column='UPD_DT')),
                ('mean_hr', models.FloatField(blank=True, db_column='HRV_MEAN_HR', null=True)),
                ('mean_rr', models.FloatField(blank=True, db_column='HRV_MEAN_RR', null=True)),
                ('sdnn', models.FloatField(blank=True, db_column='HRV_SDNN', null=True)),
                ('rmssd', models.FloatField(blank=True, db_column='HRV_RMSSD', null=True)),
                ('pnn50', models.FloatField(blank=True, db_column='HRV_pNN50', null=True)),
                ('pnn20', models.FloatField(blank=True, db_column='HRV_pNN20', null=True)),
                ('pnn10', models.FloatField(blank=True, db_column='HRV_pNN10', null=True)),
                ('pnn05', models.FloatField(blank=True, db_column='HRV_pNN05', null=True)),
                ('vlf', models.FloatField(blank=True, db_column='HRV_VLF', null=True)),
                ('lf', models.FloatField(blank=True, db_column='HRV_LF', null=True)),
                ('hf', models.FloatField(blank=True, db_column='HRV_HF', null=True)),
                ('lf_hf_ratio', models.FloatField(blank=True, db_column='HRV_LF_HF_RATIO', null=True)),
                ('sd1', models.FloatField(blank=True, db_column='HRV_SD1', null=True)),
                ('sd2', models.FloatField(blank=True, db_column='HRV_SD2', null=True)),
                ('sd1_sd2_ratio', models.FloatField(blank=True, db_column='HRV_SD1_SD2_RATIO', null=True)),
            ],
            options={
                'db_table': 'OC_HRV_RECOVERY_1',
            },
        ),
        migrations.CreateModel(
            name='Recovery2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_dt', models.DateTimeField(auto_now_add=True, db_column='INS_DT')),
                ('upt_dt', models.DateTimeField(auto_now=True, db_column='UPD_DT')),
                ('mean_hr', models.FloatField(blank=True, db_column='HRV_MEAN_HR', null=True)),
                ('mean_rr', models.FloatField(blank=True, db_column='HRV_MEAN_RR', null=True)),
                ('sdnn', models.FloatField(blank=True, db_column='HRV_SDNN', null=True)),
                ('rmssd', models.FloatField(blank=True, db_column='HRV_RMSSD', null=True)),
                ('pnn50', models.FloatField(blank=True, db_column='HRV_pNN50', null=True)),
                ('pnn20', models.FloatField(blank=True, db_column='HRV_pNN20', null=True)),
                ('pnn10', models.FloatField(blank=True, db_column='HRV_pNN10', null=True)),
                ('pnn05', models.FloatField(blank=True, db_column='HRV_pNN05', null=True)),
                ('vlf', models.FloatField(blank=True, db_column='HRV_VLF', null=True)),
                ('lf', models.FloatField(blank=True, db_column='HRV_LF', null=True)),
                ('hf', models.FloatField(blank=True, db_column='HRV_HF', null=True)),
                ('lf_hf_ratio', models.FloatField(blank=True, db_column='HRV_LF_HF_RATIO', null=True)),
                ('sd1', models.FloatField(blank=True, db_column='HRV_SD1', null=True)),
                ('sd2', models.FloatField(blank=True, db_column='HRV_SD2', null=True)),
                ('sd1_sd2_ratio', models.FloatField(blank=True, db_column='HRV_SD1_SD2_RATIO', null=True)),
            ],
            options={
                'db_table': 'OC_HRV_RECOVERY_2',
            },
        ),
        migrations.CreateModel(
            name='Stimulation1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_dt', models.DateTimeField(auto_now_add=True, db_column='INS_DT')),
                ('upt_dt', models.DateTimeField(auto_now=True, db_column='UPD_DT')),
                ('mean_hr', models.FloatField(blank=True, db_column='HRV_MEAN_HR', null=True)),
                ('mean_rr', models.FloatField(blank=True, db_column='HRV_MEAN_RR', null=True)),
                ('sdnn', models.FloatField(blank=True, db_column='HRV_SDNN', null=True)),
                ('rmssd', models.FloatField(blank=True, db_column='HRV_RMSSD', null=True)),
                ('pnn50', models.FloatField(blank=True, db_column='HRV_pNN50', null=True)),
                ('pnn20', models.FloatField(blank=True, db_column='HRV_pNN20', null=True)),
                ('pnn10', models.FloatField(blank=True, db_column='HRV_pNN10', null=True)),
                ('pnn05', models.FloatField(blank=True, db_column='HRV_pNN05', null=True)),
                ('vlf', models.FloatField(blank=True, db_column='HRV_VLF', null=True)),
                ('lf', models.FloatField(blank=True, db_column='HRV_LF', null=True)),
                ('hf', models.FloatField(blank=True, db_column='HRV_HF', null=True)),
                ('lf_hf_ratio', models.FloatField(blank=True, db_column='HRV_LF_HF_RATIO', null=True)),
                ('sd1', models.FloatField(blank=True, db_column='HRV_SD1', null=True)),
                ('sd2', models.FloatField(blank=True, db_column='HRV_SD2', null=True)),
                ('sd1_sd2_ratio', models.FloatField(blank=True, db_column='HRV_SD1_SD2_RATIO', null=True)),
            ],
            options={
                'db_table': 'OC_HRV_STIMULATION_1',
            },
        ),
        migrations.CreateModel(
            name='Stimulation2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_dt', models.DateTimeField(auto_now_add=True, db_column='INS_DT')),
                ('upt_dt', models.DateTimeField(auto_now=True, db_column='UPD_DT')),
                ('mean_hr', models.FloatField(blank=True, db_column='HRV_MEAN_HR', null=True)),
                ('mean_rr', models.FloatField(blank=True, db_column='HRV_MEAN_RR', null=True)),
                ('sdnn', models.FloatField(blank=True, db_column='HRV_SDNN', null=True)),
                ('rmssd', models.FloatField(blank=True, db_column='HRV_RMSSD', null=True)),
                ('pnn50', models.FloatField(blank=True, db_column='HRV_pNN50', null=True)),
                ('pnn20', models.FloatField(blank=True, db_column='HRV_pNN20', null=True)),
                ('pnn10', models.FloatField(blank=True, db_column='HRV_pNN10', null=True)),
                ('pnn05', models.FloatField(blank=True, db_column='HRV_pNN05', null=True)),
                ('vlf', models.FloatField(blank=True, db_column='HRV_VLF', null=True)),
                ('lf', models.FloatField(blank=True, db_column='HRV_LF', null=True)),
                ('hf', models.FloatField(blank=True, db_column='HRV_HF', null=True)),
                ('lf_hf_ratio', models.FloatField(blank=True, db_column='HRV_LF_HF_RATIO', null=True)),
                ('sd1', models.FloatField(blank=True, db_column='HRV_SD1', null=True)),
                ('sd2', models.FloatField(blank=True, db_column='HRV_SD2', null=True)),
                ('sd1_sd2_ratio', models.FloatField(blank=True, db_column='HRV_SD1_SD2_RATIO', null=True)),
            ],
            options={
                'db_table': 'OC_HRV_STIMULATION_2',
            },
        ),
        migrations.CreateModel(
            name='HRV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('int_dt', models.DateTimeField(auto_now_add=True, db_column='INS_DT')),
                ('upt_dt', models.DateTimeField(auto_now=True, db_column='UPD_DT')),
                ('measurement_date', models.DateTimeField(db_column='MEASUREMENT_DATE')),
                ('baseline', models.ForeignKey(db_column='HRV_BASELINE_ID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrv', to='ecg.baseline')),
                ('recovery1', models.ForeignKey(db_column='HRV_RECOVERY_1_ID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrv', to='ecg.recovery1')),
                ('recovery2', models.ForeignKey(db_column='HRV_RECOVERY_2_ID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrv', to='ecg.recovery2')),
                ('stimulation1', models.ForeignKey(db_column='HRV_STIMULATION_1_ID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrv', to='ecg.stimulation1')),
                ('stimulation2', models.ForeignKey(db_column='HRV_STIMULATION_2_ID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrv', to='ecg.stimulation2')),
                ('subject', models.ForeignKey(db_column='SUBJECT_ID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hrv', to='subjects.subject')),
            ],
            options={
                'db_table': 'OC_HRV',
            },
        ),
    ]
