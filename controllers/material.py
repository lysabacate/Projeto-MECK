from flask import render_template, request, redirect, flash, session
from models.turma import Turma
from models.usuario import Usuario
from models.material import Material
from utils import db, lm
from flask import Blueprint
from flask_login import login_user, logout_user, login_required, current_user
import hashlib

bp_materiais = Blueprint("materiais", __name__, template_folder='templates')


