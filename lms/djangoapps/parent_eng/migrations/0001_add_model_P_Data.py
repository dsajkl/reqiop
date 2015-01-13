# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'P_Data'
        db.create_table('parent_eng_p_data', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('studentid', self.gf('django.db.models.fields.BigIntegerField')()),
            ('studentemail', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parentname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parentemail', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parentphone', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal('parent_eng', ['P_Data'])


    def backwards(self, orm):
        # Deleting model 'P_Data'
        db.delete_table('parent_eng_p_data')


    models = {
        'parent_eng.p_data': {
            'Meta': {'object_name': 'P_Data'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parentemail': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parentname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parentphone': ('django.db.models.fields.BigIntegerField', [], {}),
            'studentemail': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'studentid': ('django.db.models.fields.BigIntegerField', [], {})
        },
        'parent_eng.parentdata': {
            'Meta': {'object_name': 'ParentData'},
            'ParentEmail': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ParentName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['parent_eng']