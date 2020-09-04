#!/usr/bin/env python
import boto3
import click

@click.command()
@click.option('--env', prompt = 'please type ste, ite, perf, or prod',
             help = 'Environment for creating new RDS')
@click.option('--release', prompt = 'please type [Y/N] to create new RDS',
             help = 'Creating new RDS')

def command(env, release):
    #config
    env = 'ite'
    ASV = ' '
    aws_profile = ' '
    Owner_contact = ' '
    CMDB_Environment = ' '
    env = env.lower()
    release = release.lower()

    #TODO : check if master Database exist if not throw runtype exception

    no_proxy= " "
    if env == '<Env>':
    region = '<Region>'
    db_instance_identifier = '<DB Name>'
    source_db_instance_identifier = '<ARN for current region>'
    tags = [
                    {'Key': 'OwnerContact', 'Value': '<OwnerContact>'},
                    {'Key': '<tag>', 'Value': '<tag>'}
    ]
    db_subnet_group_name = '<subnet group name of DB>'
    vpc_security_group_ids = '<vpc security group name>'
    kms_key_id = '<kms key id>'
    source_region = '<region>'

    elif env == '<Env>':
        region = '<Region>'
    db_instance_identifier = '<DB Name>'
    source_db_instance_identifier = '<ARN for current region>'
    tags = [
                    {'Key': 'OwnerContact', 'Value': '<OwnerContact>'},
                    {'Key': '<tag>', 'Value': '<tag>'}
    ]
    db_subnet_group_name = '<subnet group name of DB>'
    vpc_security_group_ids = '<vpc security group name>'
    kms_key_id = '<kms key id>'
    source_region = '<region>'

    else:
        raise RuntimeError(env+ 'is not a valid Environment')

    client = boto3.Session(profile_name = aws_profile, region_name = region).client('rds')
    response = client.create_db_instance_read_replica(
        DBInstanceIdentifier=db_instance_identifier,
        SourceDBInstanceIdentifier=source_db_instance_identifier,
        AutoMinorVerisonUpgrade=True,
        PublicAccessible=False,
        Tags=tags,
        DBSubnetGroupName=db_subnet_group_name,
        VpcSecurityGroupIds=vpc_security_group_ids,
        KmsKeyId=kms_key_id,
        SourceRegion=source_region
        )
    print('RDS is Created')
command()
        