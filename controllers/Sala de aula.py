from flask import render_template, request, redirect, flash
from models.Usuario import Usuario
from utils import db
from flask import Blueprint