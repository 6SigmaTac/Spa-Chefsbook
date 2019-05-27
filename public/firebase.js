var firebaseConfig = {};
firebase.initializeApp(firebaseConfig);
var database = firebase.database();


// null == not logged
window.userEmail = null;

function createErrorObject(errorCode, errorMessage) {
    return {
        code: errorCode,
        message: errorMessage
    };
}

function registerByEmail(email, password, onOk, onError) {
    firebase.auth().createUserWithEmailAndPassword(email, password)
        .then(() => {
            onOk();
        })
        .catch(error => {
            const toReturn = createErrorObject(error.code, error.message);
            onError(toReturn);

        });
}

function loginByEmail(email, password, onOk, onError) {
    firebase.auth().signInWithEmailAndPassword(email, password)
        .then(() => {
            onOk(email);
            window.userEmail = email;
        })
        .catch(error => {
            const toReturn = createErrorObject(error.code, error.message);
            onError(toReturn);

        });
}

function loginByGoogle(onOk, onError) {
    var provider = new firebase.auth.GoogleAuthProvider();
    firebase.auth().signInWithPopup(provider)
        .then(function (result) {
            var token = result.credential.accessToken;
            var user = result.user;
            onOk(user.email);
            window.userEmail = user.email;
        }).catch(function (error) {
        // TODO: additional info, maybe helpful?
        var email = error.email;
        var credential = error.credential;
        const toReturn = createErrorObject(error.code, error.message);
        onError(toReturn);

    });
}

function saveOrder(orderId, order) {
    firebase.database().ref('order/' + orderId).set(order);
}

function addOrder(order) {
    firebase.database().ref('order/').push({
        status: 'INITIALIZED',
        table: order.table,
        meals: order.meals,
        assigned: order.assigned,
        totalPrice: order.totalPrice // * 100!!!
    });
}

function getAllOrder(onSuccess) {
    return firebase.database().ref('/order/')
        .once('value')
        .then(function (snapshot) {
            onSuccess(snapshot.val());
        });
}