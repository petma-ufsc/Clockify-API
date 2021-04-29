from orator import DatabaseManager, Model, Schema
from models import *

schema = Schema(db)

schema.drop('member')
schema.drop('category')
schema.drop('project')
schema.drop('activity')
schema.drop('time_entry')

with schema.create("member") as table:
    table.increments("id")
    table.string("clockify_id").unique().nullable()
    table.string("name")
    table.string("email")
    table.timestamps()

with schema.create('category') as table:
    table.increments('id')
    table.string('clockify_id').unique().nullable()
    table.string('name')
    table.timestamps()

with schema.create('project') as table:
    table.increments('id')
    table.string('clockify_id').unique().nullable()
    table.integer('category_id').unsigned()
    table.foreign('category_id').references('id').on('category')
    table.string('name')
    table.timestamps()

with schema.create('activity') as table:
    table.increments('id')
    table.string('name')
    table.timestamps()

with schema.create('time_entry') as table:
    table.increments('id')
    table.string('clockify_id').unique().nullable()
    table.integer('member_id').unsigned()
    table.foreign('member_id').references('id').on('member')
    table.integer('project_id').unsigned()
    table.foreign('project_id').references('id').on('project')
    table.integer('activity_id').unsigned().nullable()
    table.foreign('activity_id').references('id').on('activity')
    table.integer('category_id').unsigned()
    table.foreign('category_id').references('id').on('category')
    table.timestamp('start')
    table.timestamp('end')
    table.string('description').nullable()
    table.timestamps()